# 3. Function that checks if a number is even or odd

# Get number from user
number = int(input("Enter number: "))

# Function definition
def even_or_odd(num):
    print("It's Even") if num % 2 == 0 else print("It's Odd")

# Function call
even_or_odd(number)