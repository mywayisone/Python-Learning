import csv

# Sample 1: contact list
contacts = [
    ["name", "email", "phone"],
    ["Alice", "alice@example.com", "1234567890"],
    ["Bob", "bob@example.com", "9876543210"]
]

# Write to CSV using writer
with open("contacts.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(contacts)

print("contacts.csv has been created.")


# Sample 2: contact dictionary
fieldnames = ["name", "email", "phone"]
data = [
    {"name": "Alice", "email": "alice@example.com", "phone" : "1234567890"},
    {"name":"Bob", "email": "bob@example.com", "phone": "9876543210"}
]

# Write to CSV using DictWriter
with open("dict_contacts.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print("dict_contacts.csv has been created.")

