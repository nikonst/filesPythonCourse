# it yields a 3-tuple (dirpath, dirnames, filenames).

import os

for root, dirs, files in os.walk("dir1"):
    print("current path:", root, " - directories in the path:", dirs, " - files in the path:", files)

