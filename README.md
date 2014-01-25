nmrename
========

Noneus' Mass Renaming Tool

help
====
Help for nmrename 0.1

USAGE:
nmrename.py: [FILES ...] [COMMAND ...] ...

Positions are indexes for the filename. Start an
index with "-", if you want to start index counting
from the end of the filename.

COMMANDS:
-h --help : Print this help output.
-d        : Rename folderstructure too. Be careful with "/"'s!
-f        : Don't ask. Just rename.
-cu       : Convert filename to upper case.
-cl       : Convert filename to lower case.
-cc       : Convert filename to camel case.
-sd #1    : Remove string #1 from all filenames.
-sr #1 #2 : Replace string #1 with string #2.
-si #1 #2 : Insert string #2 at position #1.
-fn #1    : Insert filecount line from #1.
-fi #1 #2 : Insert filecount line from #2 at position #1.
-exif #1  : Rename from EXIF-Data with a pattern. (e.g. %Y.%M.%D_%h:%m:%s_%O%e)
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
-tag #1   : Rename from audio tags with a pattern. (e.g. "%a - %A - %t - %y%e")
            Pattern Elements:
              %a: artist
              %A: album
              %AA: albumartist
              %t: title
              %y: year
              %tn: track-number
              %Tn: total-tracks
              %e: file extension
