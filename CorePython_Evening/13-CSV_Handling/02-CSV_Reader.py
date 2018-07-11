import csv

with open('file_2.csv') as file:
    reader = csv.reader(file)

    for data in reader:
        print(data)
