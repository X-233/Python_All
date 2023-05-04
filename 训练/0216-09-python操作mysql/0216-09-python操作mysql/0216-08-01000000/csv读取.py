import csv

with open('changsha.csv', mode='r', encoding='gbk') as file:
    csv_file = csv.reader(file)
    for item in csv_file:
        print(item)
