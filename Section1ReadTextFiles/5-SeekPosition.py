fileObject = open("alphabet.txt","r")

fileObject.seek(5)
print(fileObject.read(1))

fileObject.seek(2)
print(fileObject.read(1))

print(fileObject.read(4))

# fileObject.seek(0,2)
# print(fileObject.read(1))

fileObject.close()

'''
In text files (those opened without a b in the mode string),
only seeks relative to the beginning of the file are allowed
(the exception being seeking to the very file end with seek(0, 2))
and the only valid offset values are those returned from the f.tell(), or zero.
Any other offset value produces undefined behaviour.

'''