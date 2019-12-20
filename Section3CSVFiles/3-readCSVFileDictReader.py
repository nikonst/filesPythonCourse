# 3. Read CSV via csv.DictReader Method and Print Specific Columns
# https://www.foxinfotech.in/2018/09/python-read-csv-columns-into-list.html

import csv

with open("data.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for lines in csv_reader:
      print('{:12}'.format(lines['name/first']),'{:12}'.format(lines['name/last']), '{:12}'.format(lines['city']))
      #print(f'lines["name/first"]','{:12}'.format(lines['name/last']), '{:12}'.format(lines['city']))

# first, classic print
# print(lines['name/first'], lines['name/last'], lines['city'])

#Python has had awesome string formatters
