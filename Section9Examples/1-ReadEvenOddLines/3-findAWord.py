str = "sculptor"

fin = open("mattise.txt")
print(fin.read())

with open("mattise.txt") as fin:
    for l in fin:
        for word in l.split(' '):
            if str in word: # no -> comma -> if word == str:
                print(l)

