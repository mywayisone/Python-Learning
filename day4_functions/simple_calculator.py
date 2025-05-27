# 🏆 Mini Project: Simple Calculator
# Create a calculator that:
# Defines functions: add(), subtract(), multiply(), divide()
# Takes user input
# Performs operation
# Returns and prints result

# add() funtion definition
def add(a, b):
    return(a + b)

# subract() function definition
def substract(a, b):
    return(a - b)

# multiply() function definition
def multiply(a, b):
    return( a * b)

# divide() function definition
def divide(a, b):
    return(a / b)

# Take input from user
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))

# Funtion calls
print(f"Addition is: {add(first_num, second_num)}")
print(f"Subtraction is: {substract(first_num, second_num)}")
print(f"Multiplication is: {multiply(first_num, second_num)}")
print(f"Division is: {divide(first_num, second_num)}")
