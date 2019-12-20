import json

with open("people.json","r") as fin:
     data = json.load(fin)

for el in data:
     print(el)

for el in data:
     print(el["name"], "has", len(el["cars"]), "cars")
