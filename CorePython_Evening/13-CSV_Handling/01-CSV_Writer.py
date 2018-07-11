# file = open('file_1.csv', 'w')
#
# data = 'Hello, world, this, is , python'
#
# file.write(str(data))

import csv

data = ["First Name, Last Name".split(','),
        "Sachin, Tendulkar".split(','),
        "John, Cena".split(','),
        "Virat, Kohli".split(',')]

with open('file_2.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter = ',')

    for line in data:
        writer.writerow(line)
