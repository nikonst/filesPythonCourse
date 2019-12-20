with open("painters.txt","w") as paintersFile:
    somePainters =["Picasso\n", "Matisse\n", "De Chirico\n"]
    for p in somePainters:
        paintersFile.writelines(p)
