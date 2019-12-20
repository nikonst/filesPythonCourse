fileObject = open("cities.txt","r")

fileContext = fileObject.read()
print(fileContext)

fileObject.close()

print(fileContext)