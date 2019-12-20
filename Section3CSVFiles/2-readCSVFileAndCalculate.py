import csv

sum_age = 0
with open('data.csv') as fcsv:
    # Skip first line
    next(fcsv, None)
    
    csvReader = csv.reader(fcsv)
    
    for row in csvReader:
        print(row[1],' ', row[3])
        sum_age = sum_age + int(row[3])

    #reset file
    fcsv.seek(0)
    next(fcsv, None)
    #count rows
    count_rows = sum(1 for row in csvReader)

print(sum_age/ count_rows)
