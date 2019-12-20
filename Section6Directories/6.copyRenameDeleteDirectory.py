# direcotry to work with: sourceDir
import os
import shutil

shutil.copytree('sourceDir','sourceDirCopied')
os.rename('sourceDirCopied', 'sourceCopied')
#os.rmdir('sourceCopied') # directory not empty
shutil.rmtree('sourceCopied')

'''
    os.rmdir() ok
    pathlib.Path.rmdir() ??
    shutil.rmtree() ok
'''

# ******************* os walk


# delete all files in a directory

# https://www.tutorialspoint.com/python/python_files_io.htm FOR OS