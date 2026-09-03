import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in file:
        print(row)