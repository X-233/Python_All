import csv

data = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 2, 3, 4], [1, 2, 2, 3, 4]]

with open('data.csv', mode='w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)