# 🧩 PART 1: Python’s try / except / else / finally
# Python gives you a way to catch and handle errors gracefully so your program doesn’t crash.

# 🔹 Basic Structure

try:
    pass    # Code that might cause an error
except ValueError:
    pass    # Code to run if there is an error
else:
    pass    # Code to run if there is NO error
finally:
    pass    # Code that always runs (even if there's an error)

# ✅ Example: Division with Error Handling
# Create a file: division.py

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Please enter only numbers.")
else:
    print("Result:", result)
finally:
    print("Operation complete.")



# 🧠 PART 2: Common Error Types You Should Know
# | Error               | When It Happens                         |
# | ------------------- | --------------------------------------- |
# | `ZeroDivisionError` | Dividing by 0                           |
# | `ValueError`        | Invalid conversion (e.g., `int("abc")`) |
# | `FileNotFoundError` | Opening a non-existent file             |
# | `TypeError`         | Wrong data type for operation           |
# | `KeyError`          | Missing key in a dictionary             |
# | `IndexError`        | Index out of range in list              |


# 🔨 PART 3: Exercise — File Reader with Safety
# Create a file: safe_reader.py

filename = input("Enter a file name to open: ")

try:
    with open(filename, "r") as f:
        print(f.read())
except FileNotFoundError:
    print("That file does not exist.")
except Exception as e:
    print("Something went wrong:", e)
else:
    print("File read successfully.")
finally:
    print("End of script.")


# 🎯 OPTIONAL: Logging Errors to a File
# Instead of printing errors, you can log them.

# Create: logger_demo.py

import logging

# Set up logging
logging.basicConfig(filename="errors.log", level=logging.ERROR)

try:
    num = int(input("Enter a number: "))
    print(10 / num)
except Exception as e:
    logging.error("An error occurred: %s", e)
    print("Something went wrong. Error logged.")


# 🛠️ Challenge Task
# Write a script called calculator.py with:

# Addition, subtraction, multiplication, division

# Input handling

# Error handling (bad input, zero division)
