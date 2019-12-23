#  shutil.copyfile(src, dst, *, follow_symlinks=True) -

# shutil.copy(src, dst, *, follow_symlinks=True)
# shutil.copy2(src, dst, *, follow_symlinks=True) [NO]
  #Identical to copy() except that copy2() also attempts to preserve file metadata.

#shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, 
 #shutil.rmtree(path, ignore_errors=False, onerror=None)
 # shutil.move(src, dst, copy_function=copy2)  AS RENAME TOO? - 

# **********************
# Archiving operations

import os
import shutil

#copy file
print(os.getcwd())
os.chdir('Section6Directories/ModuleSHUTIL')
print(os.getcwd())
print(os.listdir())

#shutil.copy('courses/science/outline.txt', 'courses/culture/')
#shutil.move('courses/culture/courseoutline.txt','courses/culture/art')
# to do -> move directory
# move -> rename
#shutil.move('courses/culture/basic-concepts.txt','courses/culture/art/bc.txt')

shutil.copytree('courses','courses-back-up')
shutil.rmtree('courses-back-up')



