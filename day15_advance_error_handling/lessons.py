# 📘 Day 15 – Robust Error Handling & Exceptions (Full Version)
# This lesson will deepen your skills and cover:

# 🔹 1. Why Handle Errors?
# Uncaught errors can crash your program. Proper handling:
# - Prevents crashes
# - Makes your code more user-friendly
# - Helps with debugging and logging

# 🔹 2. Syntax Overview

# try:
#     risky_code()
# except SpecificError:
#     handle_it()
# except AnotherError as e:
#     print(f"Error: {e}")
# else:
#     run_if_no_error()
# finally:
#     always_run_this()

# 🔹 3. Common Exceptions

# | Exception           | Description                        |
# | ------------------- | ---------------------------------- |
# | `ZeroDivisionError` | Dividing by zero                   |
# | `ValueError`        | Wrong type/value (e.g. int("abc")) |
# | `FileNotFoundError` | File does not exist                |
# | `TypeError`         | Wrong type used                    |
# | `IndexError`        | List index out of range            |
# | `KeyError`          | Dict key does not exist            |


# 🔹 4. Raising Your Own Errors
# You can create your own errors with raise:
def withdraw(amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")


# 🔹 5. Custom Exceptions
class NegativeAmountError(Exception):
    pass

def deposit(amount):
    if amount < 0:
        raise NegativeAmountError("Can't deposit negative money!")

# 🔹 6. with Statement & Context Managers
with open("file.txt", "r") as f:
    data = f.read()

# Why it’s useful:
# - Automatically closes files
# - Cleaner and safer


# 🔸 Practice Task – Build a Smart Calculator 🧮
# Features:

# - Ask user for two numbers and an operation (+, -, *, /)
# - Use try...except to catch:
#   - Invalid number input
#   - Division by zero
#   - Unsupported operation
# - Add a custom exception: UnsupportedOperationError

# Bonus:
# - Use a loop so the user can keep using the calculator until they type exit