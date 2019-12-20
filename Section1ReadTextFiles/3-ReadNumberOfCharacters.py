fileObject = open("alphabet.txt","r")

print(fileObject.read(2))
print(fileObject.read(5))
print(fileObject.read(3))

fileObject.close()
