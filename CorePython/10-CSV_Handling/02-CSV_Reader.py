import csv
import pandas as pd

# with open('data_1.csv') as file:
#     reader = csv.reader(file)
#
#     for data in reader:
#         print(data)

data = pd.read_csv('data_1.csv')
print(data)
