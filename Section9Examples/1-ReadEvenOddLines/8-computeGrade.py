import csv

gradesList =[]
with open('grades.csv') as csvFile:
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        print(row)
        avg = (int(row[3]) + int(row[4]) + int(row[5])) // 3
        print(avg)
        row.append(str(avg))
        if avg >= 75:
            row.append('Pass')
        else:
            row.append('Fail')
        print(row)
        gradesList.append(row)

with open('grades.csv', 'w') as newDataFile:
    csvWriter = csv.writer(newDataFile)
    for line in gradesList:
        csvWriter.writerow(line)

