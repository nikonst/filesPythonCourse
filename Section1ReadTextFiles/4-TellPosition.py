fileObject = open("alphabet.txt","r")

print(fileObject.read(2))
print(fileObject.tell())
print(fileObject.read(5))
print(fileObject.tell())
print(fileObject.read(3))
print(fileObject.tell())

fileObject.close()