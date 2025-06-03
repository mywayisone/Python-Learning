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
