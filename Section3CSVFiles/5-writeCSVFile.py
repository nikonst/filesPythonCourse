import csv

with open('employees.csv', 'w') as employeesFile:
    csvWriter = csv.writer(employeesFile, delimiter=',')

    csvWriter.writerow(['Full Name', 'Job Title', 'Company Name'])
    csvWriter.writerow(['Tris Enderlein', 'Administrative Assistant IV', 'NoveHickle-Dickens'])
    csvWriter.writerow(['Erica Meyers', 'Structural Engineer', 'MaParker, White and Schmidt'])
    csvWriter.writerow(['Barrett Hildred', 'Tax Accountantr', 'Harris-Barton'])

#https://jsonplaceholder.typicode.com/

#write header?
