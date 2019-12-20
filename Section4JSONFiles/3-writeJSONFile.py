# The built-in json package has the magic code that transforms your Python 
# dict object in to the serialized JSON string.

import json

dataList = []

dataList.append({
     "name":"John", "age":30, "cars": ["Ford", "BMW"]
})

dataList.append({
     "name":"Mary", "age":27, "cars": ["Audi"]
})

dataList.append({
     "name":"Helen", "age":31, "cars": ["Renault", "VW", "Toyota"]
})

print(dataList)

with open("people.json","w") as fout:
    json.dump(dataList, fout)
    # json.dump(dataList, fout, indent=4)
