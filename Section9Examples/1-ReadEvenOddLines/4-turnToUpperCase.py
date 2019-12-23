lines = []
with open("lowerCaseMattise.txt") as fin:
    for l in fin:
        #print(l.upper())
        lines.append(l.upper())

print(lines)

fout = open("upperCaseMattise.txt", "w")
fout.writelines(lines)
fout.close()

