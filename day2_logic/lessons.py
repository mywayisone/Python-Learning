# 📘 Day 2: Operators, Conditions & Logic
# 🎯 Objectives:
# Understand Python's operators

# Write programs with decision-making logic

# Practice basic conditional structures
# _____________________________________________


# 🧩 1. Operators in Python

#  - ➕ Arithmetic Operators 
#     These are: +, -, *, /, %, //, **
#     Examples:

a = 10
b = 3
print(a + b)   # 13
print(a // b)  # 3 (floor division)
print(a ** b)  # 1000 (exponent)


# 🧪 Assignment Operators
#   These are: =, +=, -=, *=, /=, //=, **=
#     Examples:

x = 5
x += 3  # x = 8
x *= 2  # x = 16

# 🧠 Comparison Operators
#   These are: ==, !=, >, <, >=, <=
#     Examples:

print(5 == 5)  # True
print(7 < 2)   # False

# 🔍 Logical Operators
#   These are: and, or, not
#     Examples:

age = 20
is_student = True

print(age > 18 and is_student)  # True
print(not is_student)           # False


# 🧠 2. Conditionals (if/elif/else)
#   These helps in controlling execution of code based using conditions
#  Example:

score = 85

if score >= 90:
    print("Excellent!")
elif score >= 70:
    print("Good job!")
else:
    print("Keep practicing!")


# 🧪 Exercises (Do These in day2_logic/ Folder)
# 1. Even or Odd Checker
# - Ask the user for a number and print whether it's even or odd.

# 2. Simple Login System
#  - Create a simple login script:
#  - Ask for username and password.
#  - Compare them to hardcoded values.
#  - Print success or failure.

# 3. Grade Checker
# Ask user for their test score (0–100) and print their grade:
#  - 90+: A
#  - 80–89: B
# - 70–79: C
# - 60–69: D
# - <60: F

# 🏆 Challenge (Optional)
# Rock-Paper-Scissors Game (2 players)
# - Player 1 and Player 2 enter their choices
# - Program prints who wins or if it’s a tie

# 📦 Deliverables
# - Create a folder: day2_logic/
# - Add .py files for each exercise
# - Push to your GitHub repo