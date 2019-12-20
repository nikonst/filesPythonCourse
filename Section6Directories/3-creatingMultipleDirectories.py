# Creating Multiple Directories

import os

#os.makedirs('alpha/beta/gamma')

try:
    os.makedirs('alpha/beta/gamma')
except:
    print('dir exists')
'''By default, os.makedirs() and Path.mkdir() raise an OSError if the target directory already exists.
This behavior can be overridden (as of Python 3.2) by passing exist_ok=True as a keyword argument when
calling each function. 
'''
import pathlib

p = pathlib.Path('2018/10/05')
# p.mkdir() dont run
p.mkdir(parents=True)
