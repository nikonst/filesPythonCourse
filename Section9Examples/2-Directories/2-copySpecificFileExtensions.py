import os

basepath = "aSite/"

entries = os.scandir(basepath)
print(entries)
for e in entries:
    print(e)

entries = os.listdir(basepath)
print(entries)
for e in entries:
    print(e)