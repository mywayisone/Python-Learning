# 📘 Day 4: Functions & Code Organization
# 🎯 Objectives:
# Learn how to define and call functions
# Understand parameters and return values
# Reuse code efficiently and write cleaner programs
# ______________________________________________________

# 🧩 1. What is a Function?
# A function is a reusable block of code that performs a specific task.

def greet():
    print("Hello!")

# Call it like this:
greet()  # Output: Hello!

# 🧠 2. Functions with Parameters

def greet(name):
    print(f"Hello, {name}!")

greet("Jane")  # Output: Hello, Jane!

# You can pass more than one argument:
def add(a, b):
    print(a + b)

add(5, 7)

# 🔄 3. Return Values
# Functions can return data.

def square(n):
    return n * n

result = square(4)
print(result)  # 16

# ⚙️ 4. Organizing Code with main()
# This is a common pattern in Python:

def main():
    print("Running program...")

if __name__ == "__main__":
    main()

# It helps make your code modular and testable.

# 🧠 __name__ and "__main__" Explained
# 🔹 __name__ is a special built-in variable in Python.
# When a Python file is executed directly, __name__ is set to "__main__".

# When a Python file is imported as a module in another file, __name__ becomes the file’s name (not "__main__").

# 📦 Why Use This?
# It lets you control what code runs automatically when a file is:
# Run directly
# Imported elsewhere


# 🧪 Exercises (In day4_functions/ folder)
# 1. Create a function to print a welcome message
# 2. Function that adds two numbers
# - Accept 2 numbers from the user
# - Return the sum
# 3. Function that checks if a number is even or odd
# 4. Multiplication Table as a Function
# - Write a function that takes a number and prints its multiplication table.

# 🏆 Mini Project: Simple Calculator
# Create a calculator that:
# Defines functions: add(), subtract(), multiply(), divide()
# Takes user input
# Performs operation
# Returns and prints result

# 💪 Bonus Task (Optional)
# Refactor your number guessing game from Day 3:
# Turn it into a function: def guessing_game():
# Call the function from main()

# 📦 Deliverables
# Create folder day4_functions/
# Save all functions and calculator app
# Push to GitHub

