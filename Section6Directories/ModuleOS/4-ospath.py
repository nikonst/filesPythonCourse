'''
This module contains some useful functions on pathnames.
The path parameters are either strings or bytes .
These functions here are used for different purposes such as for merging,
normalizing and retrieving path names in python
'''

import os

out = os.path.basename("/dir1/dir2/dir3")
print(out)

out = os.path.dirname("/dir1/dir2/dir3")
print(out)

out = os.path.basename(os.getcwd())
print(out)
out = os.path.dirname(os.getcwd())
print(out)

path1 = '/alpha'
path2 = 'beta/gamma'
out = os.path.join(path1,path2)
print(out)

