import json

with open("data.json") as f:
    data = json.load(f)

#print each line
for el in data:
    print(el)

#count Males and Females
countFemale = 0
countMale = 0

for el in data:
    if el['gender'] == 'Female':
        countFemale = countFemale + 1
    elif el['gender'] == 'Male':
        countMale = countMale + 1
    else:
        pass

print("Females:",countFemale," Males:", countMale)

