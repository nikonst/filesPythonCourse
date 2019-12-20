import csv

with open('data.csv') as csvFile:
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        print(row)
 
 #/usr/lib/python3.5 -> a .py file

 