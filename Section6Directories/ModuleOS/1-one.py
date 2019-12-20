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
    print("Couldnt make dirs")

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
    print(s.stat())
    print("")
#delete af file
#os.remove("test.txt")





#cd in/up
#  os.chdir(path)

# os.chmod(path, mode, *, dir_fd=None, follow_symlinks=True)

#walk

'''
https://docs.python.org/3.8/library/os.html?highlight=os#os.getcwd


os.listdir -
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

*** no copy file
*** no move file

*** os.path.----  **********
'''
