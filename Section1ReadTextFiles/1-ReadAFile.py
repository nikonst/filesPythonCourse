fileObject = open("cities.txt","r")

print(fileObject.read())

print("Name of the file: ", fileObject.name)
print("Opening mode : ", fileObject.mode)
print("Closed: ", fileObject.closed) #open?

fileObject.close()

print("Closed: ", fileObject.closed)
