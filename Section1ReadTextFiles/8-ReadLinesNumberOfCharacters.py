fileObject = open("quotes.txt")

# Do not return the next line if the total number of returned bytes ar more than 65:
print(fileObject.readlines(65))

fileObject.close()