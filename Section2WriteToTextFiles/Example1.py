#Copy file
try:
    with open("museumsInLondon.txt", "r") as fileIn:
        with open("copiedMuseumsInLondon.txt", "w") as fielOut:
            for line in fileIn:
                fileOut.write(line)
except:
    print("No such file in current directory")
