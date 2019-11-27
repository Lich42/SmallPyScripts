#! python3

#This is a small script I made that really has no purpose.
#It gets the file size of a file, not much else to it.  Currently only works for Linux.

import os

uPath = input('Please type the full path to the dir the file is in (e.g. /home/USERNAME/Desktop/): ')
uFile = input('Please type the name of the file including the extension: ')

if uPath.endswith('/'):
    uFull = uPath +  uFile
else:
    uFull = uPath + '/' + uFile

size = os.path.getsize(uFull)

#This converts regular old bytes to kilo, mega, or gigabytes
if size < 1000:
    print(str(size) + ' Bytes')
elif size >= 1000:
    size = size / 1000
    print(str(size) + ' KB')
elif size >= 1000000:
    size = size / 1000000
    print(str(size) + ' MB')
elif size >= 1000000000:
    size = size / 1000000000
    print(str(size) + ' GB')
