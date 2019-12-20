#Use different delimeter

import csv

with open('data2.csv') as csvFile:
    csvReader = csv.DictReader(csvFile, delimiter=':')
    for row in csvReader:
        print(row)
