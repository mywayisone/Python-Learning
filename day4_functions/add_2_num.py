# 2. Function that adds two numbers
# - Accept 2 numbers from the user
# - Return the sum

# First method - Input captured after function call
def add():
    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the second number: "))
    return( first_num + second_num)

print(add())

# Second method - Input captured before function call
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))

def add(a, b):
    return a + b
print(add(first_num, second_num))