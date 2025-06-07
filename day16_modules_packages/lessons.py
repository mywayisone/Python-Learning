# 🔹 Day 16: Python Modules & Packages
# You’ll learn:

# 1. What are modules?
# - Reusing code with .py files
# - Importing standard and custom modules

# 2. What are packages?
# - Organizing large projects
# - Using __init__.py files
# - Folder-level structure

# 3. from module import function vs import module

# 4. Third-party modules recap (e.g., how colorama and prettytable were imported)

# 5. Creating your own package
# - You’ll create a calculator_utils module and reuse it



# 📝 Practice Task

# - Build a simple project where:
# - You define a main script (main.py)
# - Import functions from a custom module (calculator_utils.py)
# - Maybe even create a subpackage if you’re up for a challenge!



# 📦 What You’ll Learn Today
# 1. What is a module in Python?
# - A .py file that contains Python code (functions, classes, variables).
# - You can import and reuse it in another script.

# Example:

# math_utils.py - File that contains the code below
def square(x):
    return x * x


# Then use it:

# main.py - File that contains the code below

# import math_utils
# print(math_utils.square(5))  # 25


# 2. What is a package?
# - A folder that contains multiple modules.
# - Must have an __init__.py file (can be empty).
# - Allows for deeper code organization.

# Structure:
# project/
# │
# ├── calculator/
# │   ├── __init__.py
# │   ├── basic_ops.py
# │   └── advanced_ops.py
# └── main.py

# In main.py:

# from calculator.basic_ops import add
# print(add(2, 3))  # 5


# 🧱 Let’s Build It Step-by-Step

# ✅ Step 1: Set Up Folder Structure
# Inside your local repo, create a folder named:
# 📁 day16_modules_packages

# Inside that, create:

# day16_modules_packages/
# │
# ├── main.py
# └── calculator/
#     ├── __init__.py
#     ├── basic_ops.py
#     └── advanced_ops.py


# ✅ Step 2: Add Functions

# 📄 basic_ops.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


# 📄 advanced_ops.py

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# ✅ Step 3: Use the Package in main.py
# 📄 main.py

# from calculator.basic_ops import add, subtract
# from calculator.advanced_ops import multiply, divide

print("Add:", add(2, 3))
print("Subtract:", subtract(5, 2))
print("Multiply:", multiply(3, 4))
print("Divide:", divide(10, 2))

# 🎯 Your Task
# - Set up the folder and files as shown.
# - Copy the code snippets above into the right files.
# - Run main.py and confirm it works.
# - Push the folder to GitHub (day16_modules_packages).


# ✅ Day 16 Continued: Deepening Your Understanding of Modules & Packages
# You’ve already:
# - Set up your package folder ✅
# - Imported from modules ✅
# - Pushed it to GitHub ✅

# Now let’s finish up with the following:
# - 📦 1. Add More Reusable Utilities
# - Let’s extend your package with a new file:

# Create: utils.py inside your package
# utils.py
def greet_user(name):
    return f"Hello, {name}! Welcome back."

def capitalize_words(text):
    return " ".join(word.capitalize() for word in text.split())

# Then import and use it in main.py:

# from mypackage import utils

# print(utils.greet_user("ade"))
# print(utils.capitalize_words("python is awesome"))

# 📘 2. Understand __init__.py
# 🔹 What it does:
# - Tells Python, “This is a package.”
# - Can be empty, or contain code to run automatically
# - Lets you simplify imports

# Edit __init__.py to include:
# from .basic_ops import add, subtract
# from .utils import greet_user

# Now in main.py you can do:
# from mypackage import add, greet_user

# print(add(5, 3))
# print(greet_user("Sam"))

# | Style              | Example                 | Use When                      |
# | ------------------ | ----------------------- | ----------------------------- |
# | Specific functions | `from math import sqrt` | Cleaner and controlled        |
# | Whole module       | `import math`           | When using many functions     |
# | Alias              | `import numpy as np`    | To shorten long names         |
# | Wildcard (`*`)     | `from math import *`    | ⚠️ Avoid — pollutes namespace |


# 🧪 What to Do Now
# 1. 🔧 Add utils.py as above

# 2. 🛠 Edit __init__.py to re-export functions

# 3. ✅ Modify main.py to use the imports

# 4. 🔄 Run main.py and verify output

# 5. ⬆️ Push updates to GitHub