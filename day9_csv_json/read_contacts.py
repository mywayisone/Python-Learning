
import csv

# Read from file using reader
with open("contacts.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Read from file using DictReader
with open("dict_contacts.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)