# Creating a Single Directory

import os

try:
    os.mkdir('someDir')
except:
    print("Directory exists")
# to be 
'''except FileExistsError as exc:
    print(exc)
'''

#DOESNT KNOW PATH
# import pathlib

# directory = Path('someDir')
# directory.mkdir()

#ERROR in interpret
# from pathlib import Path

# directory = Path('someDir')
# directory.mkdir()

from pathlib import Path

directory = Path('someDir')
try:
    directory.mkdir()
except FileExistsError as exc:
    print(exc)
