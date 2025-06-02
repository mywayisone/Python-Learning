# 🧩 Part 1: CSV Basics in Python
# 📌 What Is a CSV File?
# A CSV (Comma-Separated Values) file is a plain text file that stores tabular data (like rows in Excel or a database).

# Example contacts.csv file:
# - name,email,phone
# - Alice,alice@example.com,1234567890
# - Bob,bob@example.com,9876543210

# ✅ Step-by-Step: Create Your First CSV Script

# 🔹 Step 1: write_contacts.py
# Create a file in your day9_csv_json/ folder called: write_contacts.py
# Paste this in:

import csv

# Sample contact list
contacts = [
    ["name", "email", "phone"],
    ["Alice", "alice@example.com", "1234567890"],
    ["Bob", "bob@example.com", "9876543210"]
]

# Write to CSV
with open("contacts.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(contacts)

print("contacts.csv has been created.")

# 🔸 The newline="" is used to prevent extra blank lines on Windows.

# 🔹 Step 2: Run It

# In your terminal, type: python write_contacts.py
# It should create a file named contacts.csv in your folder.

# 🔹 Step 3: read_contacts.py
# Now create this file to read the CSV:

import csv

with open("contacts.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Run it — you should see rows printed like:

['name', 'email', 'phone']
['Alice', 'alice@example.com', '1234567890']
['Bob', 'bob@example.com', '9876543210']
