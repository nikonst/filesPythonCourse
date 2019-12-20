# fileObject = open("sfomefile.txt","r")
# print(fileObject.readlines())

try:
    fileObject = open("sfomefile.txt","r")
except:
    print("Can't open the file")
    
