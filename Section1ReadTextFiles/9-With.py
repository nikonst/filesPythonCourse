with open('quotes.txt', 'r') as fileOject: 
    print(fileOject.readlines())
print(fileOject.closed)

#Another way
fileObject2 = open('quotes.txt', 'r')
with fileObject2: 
    print(fileObject2 .readlines())
print(fileObject2.closed)