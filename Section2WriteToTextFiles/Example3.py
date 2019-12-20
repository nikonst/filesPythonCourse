#Write numbers and powers as text

numberList = range(10)
for i in numberList:
    print(i)

with open("numbers.txt", "w") as fileNumbers:
    for i in numberList:
        line = str(i) + ' ' + str(i**2) + '\n'
        fileNumbers.write(line)

with open("numbers.txt", "r") as fileNumbers:
    print(fileNumbers.read())

