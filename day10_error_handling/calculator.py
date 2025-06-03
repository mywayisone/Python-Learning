# 🛠️ Challenge Task
# Write a script called calculator.py with:

# Addition, subtraction, multiplication, division

# Input handling

# Error handling (bad input, zero division)
import logging

# Set up error log
logging.basicConfig(filename="errors.log", level=logging.ERROR)

# Define menu() function
def menu():
    print("1 - Addition computation")
    print("2 - Subtraction computation")
    print("3 - Multiplication computation")
    print("4 - Division computation")

# Define addition() function

def addition():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 + num2
    except ValueError as e:
        logging.error("An error occured: %s", e)
        print("Only digit is allowed")
    except Exception as e:
        logging.error("An error occured: %s", e)
        print("Something went wrong: %s", e) 
    else:
        print(f"Sum is {result}")
    finally:
        print("Computation ended.")

# Define subtraction() function
def subtraction():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 - num2
    except ValueError:
        logging.error("An error occured: %s", e)
        print("Only digit is allowed")
    except Exception as e:
        logging.error("An error occured: %s", e)
        print("Something went wrong: %s", e) 
    else:
        print(f"Result is {result}")
    finally:
        print("Computation ended.")

# Define multiplication() function
def multiplication():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 * num2
    except ValueError as e:
        logging.error("An error occured: %s", e)
        print("Only digit is allowed")
    except Exception as e:
        logging.error("An error occured: %s", e)
        print("Something went wrong: %s", e) 
    else:
        print(f"Product is {result}")
    finally:
        print("Computation ended.")

# Define division() function
def division():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 / num2
    except ValueError as e:
        logging.error("An error occured: %s", e)
        print("Only digit is allowed")
    except ZeroDivisionError as e:
        logging.error("An error occured: %s", e)
        print("Division by zero is not allowed")
    except Exception as e:
        logging.error("An error occured: %s", e)
        print("Something went wrong: %s", e) 
    else:
        print(f"Sum is {result}")
    finally:
        print("Computation ended.")

# Define main() function
def main():
    menu()
    try:
        userinput = int(input("Enter the computation by number e.g 1 or 2: "))
    except ValueError:
        print("Only digit is allowed")
    else:
        if userinput == 1:
            addition()
        elif userinput == 2:
            subtraction()
        elif userinput == 3:
            multiplication()
        elif userinput == 4:
            division()
        else: print("Enter a valid number")

# Define the entry point
if __name__ == "__main__":
    main()