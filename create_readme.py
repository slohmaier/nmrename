#!/usr/bin/env python3
#This file creates the README

import os

readmepath = 'README.md'
nmrenamepath = 'nmrename.py'

if os.path.isfile(readmepath):
	os.remove(readmepath)
readmef = open(readmepath, 'w')

readmef.write('''nmrename
========

Noneus' Mass Renaming Tool

help
====
''')

helptext = os.popen('python3 ' + nmrenamepath + ' -h').read()

readmef.write(helptext.replace(' ', '&nbsp;').replace('\n', '<br />\n'))

readmef.close()
