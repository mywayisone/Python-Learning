# 4. Multiplication Table as a Function
# - Write a function that takes a number and prints its multiplication table.

#  Get the number from the user
limit = int(input("Enter the limit of the multiplication table: "))

# Function definition 
def multiplication(limit):
    for i in range(1, limit + 1):
        for j in range(1, 13):
            print(f"{i} * {j} = {i * j}")
        print("\n")

# Function call
multiplication(limit)