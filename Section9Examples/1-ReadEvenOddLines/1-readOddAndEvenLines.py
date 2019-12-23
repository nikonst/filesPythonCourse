print("Odd Lines")
with open("text.txt") as fin:
    count = 0
    for line in fin:
        count += 1
        if count % 2 != 0:
            print(line)

print("Even Lines")
with open("text.txt") as fin:
    count = 0
    for line in fin:
        count += 1
        if count % 2 == 0:
            print(line)

