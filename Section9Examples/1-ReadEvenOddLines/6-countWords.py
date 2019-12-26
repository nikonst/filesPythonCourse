str = "sculptor"

fin = open("finn.txt")
print(fin.read())
fin.close()

count = 0
with open("finn.txt") as fin:
    for l in fin:
        for word in l.split(' '):
            count +=1

print("Total Word Count =", count)

count = 0
wordToCount = "Huck"
with open("finn.txt") as fin:
    for l in fin:
        if wordToCount in l.split(' '):
            count +=1

print("Total count for the word '{}' is {}".format(wordToCount, count))
