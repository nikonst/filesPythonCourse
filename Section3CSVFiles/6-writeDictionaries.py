# write dictionary
# to write csv file with Dict Writer
import csv

fields = ['fruit', 'season', 'color']

fruitsArray = []
fruitsArray.append({'fruit': 'apple', 'season': 'fall', 'color': 'red'});
fruitsArray.append({'fruit': 'lemon', 'season': 'winter', 'color': 'yellow'});
fruitsArray.append({'fruit': 'avocado', 'season': 'spring', 'color': 'green'});
fruitsArray.append({'fruit': 'nectarine', 'season': 'summer', 'color': 'yellow'});
fruitsArray.append({'fruit': 'plume', 'season': 'summer', 'color': 'purple'});

fruitsFile = open('fruits.csv','w')

csvWriter = csv.DictWriter(fruitsFile, delimiter=',', fieldnames=fields)

fieldsDict = dict((field,field) for field in fields)
print(fieldsDict)
csvWriter.writerow(fieldsDict)

for row in fruitsArray:
     csvWriter.writerow(row)

fruitsFile.close()
