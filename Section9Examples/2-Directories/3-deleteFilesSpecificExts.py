import os

for root, dirs, files in os.walk("testDir"):
    print("current path:", root, " - directories in the path:", dirs, " - files in the path:", files)

print('*'*20)
for root, dirs, files in os.walk("testDir"):
    if files:
        for f in files:
            if f.endswith(".txt"):
                print(os.path.join(root, f))

#https://thispointer.com/python-how-to-remove-files-by-matching-pattern-wildcards-certain-extensions-only/

'''
 os.path.join(path, *paths)

    Join one or more path components intelligently. The return value is the concatenation of path and any members of 
    *paths with exactly one directory separator (os.sep) following each non-empty part except the last,
    meaning that the result will only end in a separator if the last part is empty. If a component is an absolute path,
    all previous components are thrown away and joining continues from the absolute path component.
'''