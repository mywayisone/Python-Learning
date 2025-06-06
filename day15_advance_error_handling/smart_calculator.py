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

def show_menu():
    print("1. - Addition computation")
    print("2. - Subtraction computation")
    print("3. - Multiplication computation")
    print("4. - Division computation")

# Define the addition() function
def addition(num1, num2):
    try:
        result = num1 + num2
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    else: return result

# Define the subtraction() function
def subtraction(num1, num2):
    try:
        result = num1 - num2
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    else: return result

# Define the multiplication() function
def multiplication(num1, num2):
    try:
        result = num1 * num2
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    else: return result

# Define the division
def division(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    else: return result

# Define custom error Exception
class UnsupportedOperationError(Exception):
    pass

# Entry point
def main():
    operators = ["+", "-", "*", "/"]
    while True:
        try:
            expression = input("Enter expression e.g (3 * 5) or exit: ")
            if expression == "exit":
                break
            expression_list = expression.split()
            num1 = float(expression_list[0])
            operator = expression_list[1]

            if operator not in operators:
                raise UnsupportedOperationError("This operation is not supported")

            num2 = float(expression_list[2])
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")
        except UnsupportedOperationError as e:
            print(f"Error: {e}")
        else:
            if operator == "+":
                print(f"Sum is: {addition(num1, num2)}")
            elif operator == "-":
                print(f"Difference is: {subtraction(num1, num2)}")
            elif operator == "*":
                print(f"Product is: {multiplication(num1, num2)}")
            else:
                print(f"Quotient is: {division(num1, num2)}")
        


if __name__ == "__main__":
    main()