import csv

data = ["First Name, Last Name".split(","),
        "Sachin, Tendulkar".split(","),
        "MS, Dhoni".split(","),
        "Virat, Kohli".split(","),
        "Harbhajan, Singh".split(",")]

with open('data_1.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter = ',')

    for d in data:
        writer.writerow(d)
