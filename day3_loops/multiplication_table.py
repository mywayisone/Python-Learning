# 4. Multiplication Table
# Ask the user for a number and print its multiplication table (1 to 12).

number = input("Enter a number: ")

if number.isdigit():
    number = int(number)
    for i in range(1, 13):
        print(f"{number} * {i} = {number * i}")
else: print("Enter a valid number")