#Delete Specific Line
lineToBeDeleted = 5

with open("text.txt") as fin:
    lines = fin.readlines()

print(lines)
newlines = lines[:lineToBeDeleted-1] + lines[lineToBeDeleted:]
print(newlines)

with open("text.txt","w") as fout:
    fout.writelines(newlines)
