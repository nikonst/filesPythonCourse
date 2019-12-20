import os
#
import pathlib

print(os.listdir('.'))

print(os.listdir('world'))
dirlist = os.listdir('world')
for l in dirlist:
    print(l) # no name attr


dirlist = os.scandir('world')

for l in dirlist:
    #print(l.name, l.path, l.is_dir(), l.is_file())
    print("Name:", l.name, "Path:", l.path, "Directory:", l.is_dir(), "File:", l.is_file())
    print("***")
    print(l.stat())

entries = pathlib.Path('world')
for entry in entries.iterdir():
    print(entry.name)

