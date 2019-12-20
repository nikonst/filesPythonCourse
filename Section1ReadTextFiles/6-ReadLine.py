fileObject = open("quotes.txt","r")

print(fileObject.readline())

print(fileObject.readline())

print(fileObject.readline())

print(fileObject.readline())
print(fileObject.readline())
print(fileObject.readline())

fileObject.seek(0)
print(fileObject.readline())

# Read & print the first 5 characters of the line
print(fileObject.readline(5))

fileObject.close()

