import os

cwd = os.getcwd()
print(cwd)

for el in os.listdir('.'):
    print(el)

#********************
os.chdir('./coredel')

cwd = os.getcwd()
print(cwd)

for el in os.listdir('.'):
    print(el)

#Copy, Move File
import shutil

shutil.copy('aFile.txt', './folder1')
os.remove('./folder2/aFile.txt')
shutil.move('./folder1/aFile.txt', './folder2')


#Delete File - To be in a new .py file
os.remove('./folder2/aFile.txt')

# To preserve all file metadata when copying, use shutil.copy2():

