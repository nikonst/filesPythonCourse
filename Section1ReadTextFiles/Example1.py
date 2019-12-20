#Read numbers from a file and do some manipulation

fo = open("numbers.txt")

for x in fo:
    print("Number:",int(x)," Double:", int(x)*2, "Square:", int(x)**2)

fo.close()
