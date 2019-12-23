lines = []
with open("lowerCaseMattise.txt") as fin:
    for l in fin:
        lCapitals = []
        for word in l.split():
            wordCapital = word.capitalize()
            lCapitals.append(wordCapital)
            joined = ' '.join(lCapitals)
        joined += str('\n')
        lines.append(joined)
    print(lines)

fout = open("upperCaseFirstLetterMattise.txt", "w")
fout.writelines(lines)
fout.close()
