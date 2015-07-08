#!/usr/bin/env python3

import os
import re
import sys


class RenamerError(BaseException):
    '''
    Represents a rename error

    members:
    msg - message
    '''

    def __init__(self, msg):
        '''
        create new RenamerError

        msg - message
        '''
        self.msg = msg

    def __str__(self):
        '''string reprensentation. returns message.'''
        return self.msg


def Renamer(_class):
    '''decorator for classes to be an IRenamer'''
    NmRename._renamers.append(_class)
    return _class


class IRenamer(object):
    '''
    Interface for renamers
    '''

    #cmdline argument
    arg = None
    #arguemtns after cmdline argument
    argcount = -1
    #helptext
    helptext = None

    def __init__(self, args):
        raise NotImplemented()

    def rename(self, old, realold):
        raise NotImplemented()

    @staticmethod
    def withrenamedict(old, renamedict):
        '''
        Rename a filename base on a renamedict.
        The keys will in the renamedict will be replaced by their values.

        old - original filename
        renamedict - dict with keys and values as str
        '''
        new = old
        for key in list(renamedict.keys()):
            new = new.replace(key, renamedict[key])
        return new


class NmRename(object):
    '''
    Main class
    '''

    #global variable that holds IRenamer-classes
    _renamers = []

    def __init__(self, args):
        '''
        Create new NmRenamer

        args - sys.argv without binary
        '''
        self._showhelp = '-h' in args or '--help' in args or len(args) == 0
        self._force = '-f' in args
        self._error = None
        self._renamedirs = '-d' in args

        #don't handle flags
        if self._force:
            args.remove('-f')
        if self._renamedirs:
            args.remove('-d')

        #if help flag set don't rename
        if not self._showhelp:
            try:
                self._pathlist = self._parse_args(args)
            except RenamerError as e:
                self._error = e

    def _parse_args(self, args):
        '''
        Parse all cmdline arguments and to the renaming
        Returns a list with tuples of (original, new)

        args - cmdline arguments
        '''
        pathlist = []
        _len = len(args)
        i = 0
        while i < _len:
            arg = args[i]

            #if argument is a file add it to pathlist
            if os.path.isfile(arg):
                print('Adding file %s' % arg)
                filetuple = (os.path.dirname(arg), os.path.basename(arg))
                pathlist.append((filetuple, filetuple))
            #only add dictories to pathlist if renamedirs flag is set
            elif self._renamedirs and os.path.isdir(arg):
                print('Adding dir %s' % arg)
                dirtuple = (os.path.dirname(arg), os.path.basename(arg))
                pathlist.append((dirtuple, dirtuple))
            #rename pathlist
            else:
                #find renmaer based on cmdline argument
                renamer = self._find_renamer(arg)
                if not renamer:
                    raise RenamerError('Argument %s is neither a file nor a valid renamerswitch' % arg)
                else:
                    #enough arguments left?
                    if _len - i - renamer.argcount < 0:
                        raise RenamerError('Not enought parameters for argument %s' % arg)

                    #rename
                    renamerargs = args[i+1:i+1+renamer.argcount]
                    print(self._get_renametext(renamer, renamerargs))
                    pathlist = self._rename(renamer(renamerargs), pathlist)

                    #correct index
                    i += renamer.argcount

            #next argument
            i += 1
        return pathlist

    @staticmethod
    def _get_renametext(renamer, args):
        '''
        Get action text for a renamer.

        renamer - IRenamer object
        args - arguments for renamer
        '''
        text = renamer.actiontext
        for arg in args:
            num = None
            try:
                num = int(arg)
            except:
                pass

            if num is not None:
                text = text.replace('?', arg, 1)
            else:
                text = text.replace('?', '"%s"' % arg, 1)
        return text

    @staticmethod
    def _find_renamer(arg):
        '''
        Get the IRenamer implementation for an argument.
        Returns None if it does not exist.

        arg - argument as str
        '''
        for renamer in NmRename._renamers:
            if renamer.arg == arg:
                return renamer
        return None

    def _rename(self, renamer, pathlist):
        '''
        Rename a pathlist and return the new one

        renamer - IRenamer implementation
        pathlist - pathlist containing tuples of old and new filename
        '''
        newpathlist = []
        for old, new in pathlist:
            newfile = renamer.rename(new[1]
                                     if not self._renamedirs else
                                     os.path.join(*new), os.path.join(*old))
            if not newfile:
                print('Ommitting %s. Would result in empty filename.' % new[1])
                newfile = new[1]
            newpathlist.append((
                    old,
                    (new[0], newfile) if not self._renamedirs
                    else (os.path.dirname(newfile), os.path.basename(newfile))
            ))
        return newpathlist

    @staticmethod
    def _print_help():
        '''Print the help text'''
        print('Help for nmrename 0.1')
        print()
        print('USAGE:')
        print('%s: [FILES ...] [COMMAND ...] ...' % sys.argv[0])
        print()
        print('Positions are indexes for the filename. Start an')
        print('index with "-", if you want to start index counting')
        print('from the end of the filename.')
        print()
        print('COMMANDS:')

        helptexts = [
            ('-h --help', 'Print this help output.'),
            ('-d', 'Rename folderstructure too. Be careful with "/"\'s!'),
            ('-f', 'Don\'t ask. Just rename.')
        ]
        maxlen = len(helptexts[0][0])
        for renamer in NmRename._renamers:
            helptexts.append(('%s%s%s' % (
                renamer.arg,
                ' ' if renamer.argcount > 0 else '',
                ' '.join(['#'+str(i) for i in range(1, 1+renamer.argcount)]),
            ), renamer.helptext))
            _len = len(helptexts[-1][0])
            if _len > maxlen:
                maxlen = _len

        for start, text in helptexts:
            print('%s : %s' % (
                start+' '*(maxlen-len(start)),
                text.strip().replace('\n', '\n'+' '*(maxlen+3))))

    def run(self):
        if self._showhelp:
            self._print_help()
            return 0

        if self._error:
            print('ERROR: %s' % str(self._error))
            return 1

        print()
        print('---PREVIEW---')
        print()
        pathlist = []
        for old, new in self._pathlist:
            if old[1] != new[1]:
                pathlist.append((os.path.join(old[0], old[1]), os.path.join(new[0], new[1])))
                print('"%s" -> "%s"' % (pathlist[-1][0], pathlist[-1][1]))

        if not pathlist:
            print('Nothing to rename.')
            return 0

        if not self._force:
            if input('Rename? [y/n] ') != 'y':
                return 0

        print('Renaming...')
        for old, new in pathlist:
            newdir = os.path.dirname(new)
            if os.path.dirname(old) == newdir:
                os.rename(old, new)
            else:
                os.makedirs(os.path.dirname(new))

        print('Done. Good Bye.')

class Field:
    '''
    Splitup fields in a string by defined delimiters
    
    delimiters is a string with a collection of delimiter characters.
    '''
    
    def __init__(self, delimiters, pos):
        '''
        Create a new field
        
        delimiters - collection of delimiter characters
        pos - position of the field
        '''
        self._delimiters = delimiters
        self._pos = pos
        
    def get_field_coords(self, s):
        '''
        Get field coordinates in the string. Returns tuple of startindex, endindex.
        
        s - string to get coordinates for
        pos - position of the field
        '''
        direction = -1 if self._pos.strip().startswith('-') else 1 #direction for iteration
        starti = len(s) -1 if direction == -1 else 0 #start in string
        endi = 0 if direction == -1 else (len(s) - 1) #end in string
        startpos = -1 #resulting start position
        endpos = -1 #resulting end position
        fieldpos = abs(int(self._pos)) #absolute field position
        
        #iterate over whole string
        i = starti
        currentf = 0
        while i != endi + direction:
            if s[i] in self._delimiters:
                #when delimiter hit count fields
                #on field change save startpos and endpos correctly
                currentf += 1
                if currentf == fieldpos:
                    startpos = i + direction
                elif currentf == fieldpos + 1:
                    endpos = i - direction
            
            i += direction
        
        #correct startpos and endpos for first and last field
        if startpos == -1 and endpos != -1:
            startpos = starti
        elif startpos != -1 and endpos == -1:
            endpos = endi
        
        #if direction is -1 correct start and endpos to other direction
        if startpos > endpos:
            temppos = endpos
            endpos = startpos
            startpos = temppos
        
        return None if startpos == -1 and endpos == -1 else (startpos, endpos) 
            
         

class Position:
    '''
    Reprents a position in a filename

    Positive number will be counted from left.
    Numbers with a minus in front from the right
    '''

    def __init__(self, pos):
        '''
        Create a new position.

        pos - position as string.
        '''
        self._from_left = not pos.startswith('-')
        self._num = int(pos) if not pos.startswith('-') else -1*int(pos)

    def get_index(self, s):
        '''
        Get index for a string.

        s - the string
        '''
        index = self._num if self._from_left else len(s) - self._num
        if index > len(s):
            index = len(s)
        if index < 0:
            index = 0
        return index


@Renamer
class RenamerUpperCase(IRenamer):
    arg = '-cu'
    argcount = 0
    helptext = 'Convert filename to upper case.'
    actiontext = 'Converting filename to upper case.'

    def __init__(self, args):
        pass

    def rename(self, old, realold):
        return old.upper()


@Renamer
class RenamerLowerCase(IRenamer):
    arg = '-cl'
    argcount = 0
    helptext = 'Convert filename to lower case.'
    actiontext = 'Converting filename to lower case.'

    def __init__(self, args):
        pass

    def rename(self, old, realold):
        return old.lower()


@Renamer
class RenamerCamelCase(IRenamer):
    arg = '-cc'
    argcount = 0
    helptext = 'Convert filename to camel case.'
    actiontext = 'Converting filename to camel case.'

    def __init__(self, args):
        pass

    def rename(self, old, realold):
        return old.title()


@Renamer
class RenamerStringDelete(IRenamer):
    arg = '-sd'
    argcount = 1
    helptext = 'Remove string #1 from all filenames.'
    actiontext = 'Removing string ? from all filenames.'

    def __init__(self, args):
        self.removee = args[0]

    def rename(self, old, realold):
        return old.replace(self.removee, '')


@Renamer
class RenamerStringReplace(IRenamer):
    arg = '-sr'
    argcount = 2
    helptext = 'Replace string #1 with string #2.'
    actiontext = 'Replacing string ? with string ?.'

    def __init__(self, args):
        self.replacee = args[0]
        self.replacer = args[1]

    def rename(self, old, realold):
        return old.replace(self.replacee, self.replacer)


@Renamer
class RenamerStringInsert(IRenamer):
    arg = '-si'
    argcount = 2
    helptext = 'Insert string #2 at position #1.'
    actiontext = 'Inserting at position ? string ?.'

    def __init__(self, args):
        self.pos = Position(args[0])
        self.fromright = args[0].startswith('-')
        self.s = args[1]

    def rename(self, old, realold):
        index = self.pos.get_index(old)
        if self.fromright:
        	index += 1
        return old[:index] + self.s + old[index:]

@Renamer
class RenamerNameFromFile(IRenamer):
    arg = '-fn'
    argcount = 1
    helptext = 'Insert filecount line from #1.'
    actiontext = 'Inserting filecount line from #1.'

    def __init__(self, args):
        f = open(args[0], 'r')
        self.lines = [line.strip() for line in f.readlines()]
        f.close()
        self.linecount = 0

    def rename(self, old, realold):
        line = self.lines[self.linecount]
        self.linecount += 1
        return line

@Renamer
class RenamerNameFromFileInsert(IRenamer):
    arg = '-fi'
    argcount = 2
    helptext = 'Insert filecount line from #2 at position #1.'
    actiontext = 'Inserting filecount line from #2 at position #1.'

    def __init__(self, args):
        self.pos = Position(args[0])
        f = open(args[1], 'r')
        self.lines = [line.strip() for line in f.readlines()]
        f.close()
        self.linecount = 0

    def rename(self, old, realold):
        index = self.pos.get_index(old)
        line = self.lines[self.linecount]
        self.linecount += 1
        return old[:index] + line + old[index:]

@Renamer
class RenamerPythonRegex(IRenamer):
    arg = '-pyr'
    argcount = 2
    helptext = 'Replace the pattern "#1" with "#2" with python regex-interpreter.\n( https://docs.python.org/library/re.html#re.sub )'
    actiontext = 'Replacing the pattern "#1" with "#2" with python regex-interpreter.'

    def __init__(self, args):
        self.regex = re.compile(args[0])
        self.replacee = args[1]

    def rename(self, old, realold):
        return self.regex.sub(self.replacee, old)

try:
    from PIL import Image
    from PIL.ExifTags import TAGS

    @Renamer
    class RenamerEXIF(IRenamer):
        arg = '-exif'
        argcount = 1
        helptext = '''
Rename from EXIF-Data with a pattern. (e.g. %Y.%M.%D_%h:%m:%s_%O%e)
Pattern Elements:
  %Y: year (e.g. 2012)
  %M: month (e.g. 06)
  %D: day (e.g. 09)
  %h: hour (e.g. 14)
  %m: minute (e.g. 40)
  %s: second (e.g. 09)
  %o: complete original filename
  %e: extension (e.g. .jpg)
  %O: filename without extension
'''
        actiontext = 'Renaming from EXIF Data with pattern ?.'

        def __init__(self, args):
            self.pattern = args[0]

        @staticmethod
        def _get_exif(filename):
            ret = {}
            i = Image.open(filename)
            info = i._getexif()

            if info:
                for tag, value in list(info.items()):
                    decoded = TAGS.get(tag, tag)
                    ret[decoded] = value
            return ret

        def rename(self, old, realold):
            exifdata = self._get_exif(realold)
            if not exifdata or not 'DateTime' in exifdata:
                print('  Omitting "%s", because of no EXIF data or missing datetime.' % realold)
                return old
            else:
                filename = os.path.basename(realold)
                basename, ext = os.path.splitext(filename)
                dt = exifdata['DateTime'].split(' ')
                dt = dt[0].split(':') + dt[1].split(':')
                return self.withrenamedict(self.pattern, {
                    '''%Y''': dt[0],
                    '''%M''': dt[1],
                    '''%D''': dt[2],
                    '''%h''': dt[3],
                    '''%m''': dt[4],
                    '''%s''': dt[5],
                    '''%o''': filename,
                    '''%e''': ext,
                    '''%O''': basename})
except:
    print('WARNING: Cannot use EXIF-renamer. Please install PIL (http://www.pythonware.com/products/pil/).')
    print()

try:
    import mutagen

    @Renamer
    class RenamerAudioTag(IRenamer):
        arg = "-tag"
        argcount = 1
        helptext = '''
Rename from audio tags with a pattern. (e.g. "%a - %A - %t - %y%e")
Pattern Elements:
  %a: artist
  %A: album
  %AA: albumartist
  %t: title
  %y: year
  %tn: track-number
  %Tn: total-tracks
  %e: file extension
'''
        actiontext = 'Renaming from audio tags with pattern ?.'

        def __init__(self, args):
            self.pattern = args[0]

        def rename(self, old, realold):
            tagdata = mutagen.File(realold, easy=True)
            if not tagdata:
                print('  Omitting "%s", because of ' % realold + \
                      'no EXIF data or missing datetime.')
                return old
            else:
                basename, ext = os.path.splitext(realold)
                return self.withrenamedict(self.pattern, {
                    '''%a''': tagdata['artist'][0]
                    if 'artist' in tagdata else 'Unkown',
                    '''%A''': tagdata['album'][0]
                    if 'album' in tagdata else 'Unkown',
                    '''%AA''': tagdata['albumartist'][0]
                    if 'albumartist' in tagdata else tagdata['artist'][0]
                    if 'artist' in tagdata else 'Unkown',
                    '''%t''': tagdata['title'][0]
                    if 'title' in tagdata else 'Unkown',
                    '''%y''': tagdata['date'][0]
                    if 'date' in tagdata else '0000',
                    '''%tn''': tagdata['tracknumber'][0]
                    if 'tracknumber' in tagdata else '0',
                    '''%TN''': tagdata['tracktotal'][0]
                    if 'tracktotal' in tagdata else '0',
                    '''%e''': ext})
except:
    print('WARNING: Cannot use audiotag-renamer. Please install Mutagen (http://code.google.com/p/mutagen/).')
    print()
    
@Renamer
class FieldDelete(IRenamer):
    arg = '-fieldd'
    argcount = 2
    helptext = 'Remove field #2 delimited by #1.'
    actiontext = 'Removing field #2 delimited by #1.'

    def __init__(self, args):
        self._field = Field(args[0], args[1])

    def rename(self, old, realold):
        fieldres = self._field.get_field_coords(old)
        if not fieldres:
            return old
        else:
            startpos = fieldres[0]-1 #correct startpos for indexing
            endpos = fieldres[1]+1 #correct endpos for indexing
            return old[:startpos] + old[endpos:]        

if __name__ == '__main__':
    sys.exit(NmRename(sys.argv[1:]).run())
