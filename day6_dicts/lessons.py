# 📘 Day 6: Dictionaries in Python
# 🎯 Objectives:
# Learn how to create and use dictionaries
# Add, update, and remove data
# Loop through keys and values
# Build practical mini-projects (like a contact book)

# 🔹 1. What is a Dictionary?
# A dictionary is a collection of key-value pairs.

person = {
    "name": "Alice",
    "age": 30,
    "location": "Lagos"
}

# ✅ Keys must be unique
# ✅ Values can be anything
# ✅ Dictionaries are unordered (in versions before 3.7), but indexed by key

# 🧠 Accessing Data
print(person["name"])       # Alice
print(person.get("email"))  # None (no error)

# ✍️ Adding / Updating Values
person["email"] = "alice@gmail.com"  # Add
person["age"] = 31                   # Update

# ❌ Removing Data
del person["location"]
person.pop("email")

# 🔁 Looping Through a Dictionary
for key in person:
    print(key, person[key])

# OR
for key, value in person.items():
    print(f"{key}: {value}")


# ✅ Dictionary Methods
# | Method        | Description               |
# | ------------- | ------------------------- |
# | `.get(key)`   | Safe access               |
# | `.keys()`     | All keys                  |
# | `.values()`   | All values                |
# | `.items()`    | Key-value pairs           |
# | `.pop(key)`   | Remove a key              |
# | `.update({})` | Add/update multiple pairs |

# 🔄 Nesting Dictionaries
students = {
    "101": {"name": "Jane", "score": 90},
    "102": {"name": "John", "score": 85}
}

print(students["101"]["name"])  # Jane



# 🔍 Advanced Python Dictionary Concepts
# 📦 1. Dictionary Recap
person = {
    "name": "Ada",
    "age": 28,
    "email": "ada@example.com"
}
# - Keys must be immutable types: str, int, float, bool, or tuple
# - Values can be any type, including lists, other dictionaries, or functions

# 🧠 2. Creating Dictionaries in Multiple Ways
# ✅ Literal syntax
d = {"a": 1, "b": 2}

# ✅ Using dict()
d = dict(a=1, b=2)  # keys must be valid identifiers

# ✅ From a list of tuples
pairs = [("a", 1), ("b", 2)]
d = dict(pairs)

# 🧰 3. Useful Dictionary Methods (Deeper Dive)
# 🔹 .get(key, default)
# Safe access — avoids KeyError.
d.get("name", "Unknown")

# 🔹 .setdefault(key, default)
# If key exists, return it. If not, create it with default.
student = {"name": "Joe"}
student.setdefault("grade", "A")  # Adds grade if missing

# 🔹 .update()
# Merge or override values.
info = {"email": "new@email.com"}
person.update(info)

# 🔹 .pop(key, default)
# Remove and return value.
email = person.pop("email", "Not found")

# 🔹 .fromkeys(iterable, value)
# Create a new dictionary with default values.
fields = dict.fromkeys(["name", "email", "phone"], None)

# 🔁 4. Looping Patterns
# Loop keys
for key in person:
    print(key)

# Loop values
for value in person.values():
    print(value)

# Loop key-value pairs
for key, value in person.items():
    print(f"{key} => {value}")

# 🧱 5. Nested Dictionaries
# These are like "records inside records."
users = {
    "001": {
        "name": "Ada",
        "email": "ada@example.com"
    },
    "002": {
        "name": "Chike",
        "email": "chike@example.com"
    }
}
print(users["001"]["name"])  # Ada
# Great for modeling databases and structured data.

# 🧪 6. Dictionary Comprehensions
# Similar to list comprehensions:
squares = {x: x * x for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Example: Count word frequency
words = ["apple", "banana", "apple", "apple", "banana"]
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)  # {'apple': 3, 'banana': 2}

# 🧰 7. Real-World Dictionary Use Cases
# | Scenario         | Dictionary Usage                         |
# | ---------------- | ---------------------------------------- |
# | User data        | Store fields like name, age, email       |
# | Inventory system | Store items with quantities/prices       |
# | Contact list     | Name as key, phone/email as value        |
# | Scoreboard       | Player names as keys, scores as values   |
# | Config files     | Option names as keys, values as settings |

# 🧠 8. Dictionary vs List — When to Use Which?
# | Feature          | List          | Dictionary                         |
# | ---------------- | ------------- | ---------------------------------- |
# | Ordered by index | ✅             | ❌ (3.6+ maintains insertion order) |
# | Search by key    | ❌ Linear time | ✅ Constant time                    |
# | Good for...      | Sequences     | Lookups, structured records        |

# 💥 Bonus Practice Ideas
# 🔍 1. Word Counter
# Input: sentence

# Output: dictionary of word frequencies

# 📦 2. Product Inventory
# products = {
#     "P001": {"name": "Laptop", "price": 4500, "stock": 5},
#     "P002": {"name": "Mouse", "price": 500, "stock": 15},
# }

# - Add new products
# - List all
# - Check stock before selling

# 📇 3. Student Grades Tracker
# - Add student name + list of scores
# - Calculate average



# 🧪 Exercises (in day6_dicts/ folder)
# 1. Create a Dictionary of a Student
# Fields: name, age, grade, email
# Print all values

# 2. Add New Key to Dictionary
# Add "phone" to the student dictionary

# 3. Create a Dictionary of 3 Books
# books = {
#     "001": {"title": "Book One", "author": "Author A"},
#     "002": {"title": "Book Two", "author": "Author B"},
#     ...
# }
# Print all titles

# 4. Loop Through a Dictionary
# Print all key-value pairs from any dictionary

# 5. Use get() to Access a Key That Might Not Exist


# 🛠️ Mini Project: Contact Book
# Features:
# - Add new contact (name, phone)
# - View all contacts
# - Search contact by name
# - Delete contact
# - Exit