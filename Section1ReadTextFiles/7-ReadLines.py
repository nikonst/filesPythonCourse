fileObject = open("quotes.txt","r")

print('List')
print(fileObject.readlines())

print("1-"*30)
fileObject.seek(0)
for line in fileObject.readlines():
    print(line)

print("2-"*30)
fileObject.seek(0)
for line in fileObject:
    print(line)

fileObject.close()

#If you want to read all the lines of a file in a list you can also use list(f) or f.readlines().
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files