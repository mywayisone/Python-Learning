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

# 📦 Working with JSON Files

# 📌 What is JSON?
# JSON stands for JavaScript Object Notation. It’s a human-readable data format used everywhere — especially in:

# - Web APIs
# - Configuration files
# - Saving structured user data
# It looks like a Python dictionary, but it's used across many languages.

# 🔍 Example: JSON vs Python Dict
# | Python `dict`                  | JSON                           |
# | ------------------------------ | ------------------------------ |
# | `{"name": "Alice", "age": 25}` | `{"name": "Alice", "age": 25}` |

# ✅ Core JSON Functions in Python
# You’ll use Python’s built-in json module:

import json

# | Task                     | Function                |
# | ------------------------ | ----------------------- |
# | Read JSON from file      | `json.load(file)`       |
# | Write JSON to file       | `json.dump(data, file)` |
# | Convert string to Python | `json.loads(string)`    |
# | Convert Python to string | `json.dumps(data)`      |

# 🛠 Your Task: JSON Settings Manager
# ✏️ Features:
# - Save settings in a JSON file
# - Load settings from file
# - Update settings and save changes

# ✅ Starter Code: settings_manager.py
import json
import os

SETTINGS_FILE = "settings.json"

# Default settings
default_settings = {
    "username": "Guest",
    "theme": "light",
    "language": "en"
}

# Load settings (or create default)
def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "w") as file:
            json.dump(default_settings, file, indent=4)
    with open(SETTINGS_FILE, "r") as file:
        return json.load(file)

# Save settings
def save_settings(settings):
    with open(SETTINGS_FILE, "w") as file:
        json.dump(settings, file, indent=4)

# Update one setting
def update_setting(key, value):
    settings = load_settings()
    settings[key] = value
    save_settings(settings)
    print(f"{key} updated to {value}.")

# Run sample menu
settings = load_settings()
print("Current Settings:", settings)

key = input("Which setting do you want to change? (username/theme/language): ").strip()
value = input("New value: ").strip()

update_setting(key, value)


# 📥 Your Turn
# Create a file called settings_manager.py in your day9_csv_json/ folder

# - Paste and modify the code above as needed
# - Run it, test updates, and view the settings.json file
# - Push your work to GitHub