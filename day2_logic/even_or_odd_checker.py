# This program checks if a number is Even or Odd number

user_input = input("Enter a number: ")
if user_input.isdigit():
    if int(user_input) == 0:
        print(f"{user_input} is neither Even nor Odd number")
    elif int(user_input) % 2 == 0:
        print(f"{user_input} is an Even number")
    else: print(f"{user_input} is an Odd number")
else: print(f"{user_input} is not a valid integer number")