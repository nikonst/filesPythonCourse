import os

#os.getcwd()
print("Current Diroctory:", os.getcwd())

#listdir()
print(os.listdir())

#mkdir
try:
    os.mkdir('subDirectory')
except:
    print("File Exists")

#rmdir
os.rmdir('subDirectory')

#makedirs
try:
    os.makedirs("sub1/sub2")
except:
    print("Couldnt make dirs")

#removedirs
try:
    os.removedirs("sub1/sub2")
except:
    print("Couldnt remove dirs")

##listdir()
print(os.listdir())

with open("test.txt","w") as f:
    f.write("Some text")

#rename file
os.rename("test.txt", "file1.txt")
os.mkdir('testDir')
os.rename('testDir', 'testOSDir')

#renames
os.renames('file1.txt','dir1/dir2/file2.txt')

#scandir
sd = os.scandir()

for s in sd:
    print(s)
    print(s.name)
    print(s.path)
    print(s.is_file())
    print(s.is_dir())
    #print(s.stat())
    print("")

#delete af file
#os.remove("test.txt")

print("Current Directory:", os.getcwd())
os.chdir('Section6Directories/ModuleOS')
print("Current Directory:", os.getcwd())
'''os.chdir('..')
print("Current Directory:", os.getcwd())
'''
try:
    os.remove('dir1/dir2/file2.txt')
except:
    print('Cant remove file')

#cd in/up
#  os.chdir(path)

# os.chmod(path, mode, *, dir_fd=None, follow_symlinks=True)

#walk

'''
https://docs.python.org/3.8/library/os.html?highlight=os#os.getcwd


os.listdir -
os.chdir -
os.mkdir -
os.makedirs - 
os.remove -
os.removedirs -
os.rename -
os.renames -
os.rmdir - 
os.scandir -
os.scandir.close() -
os.stat -

''' 

'''
Using String Methods

>>> import os

>>> # Get .txt files
>>> for f_name in os.listdir('some_directory'):
...     if f_name.endswith('.txt'):
...         print(f_name)


https://realpython.com/working-with-files-in-python/#listing-all-files-in-a-directory
Simple Filename Pattern Matching Using fnmatch
More Advanced Pattern Matching
Traversing Directories and Processing Files
'''

'''
*** no copy file
*** no move file




*** os.path.----  **********
'''
