# 3. Sum of Numbers
# Ask the user for a number n and calculate the sum from 1 to n.


sum = 0
number = input("Enter a number: ")
if number.isdigit():
    print("\nFirst Method\n")
    number = int(number)
    sum = number * (number + 1) // 2
    print(f"Sum is {sum}")

    print("\n Second Method \n")

    sum = 0
    for i in range(1, number + 1):
        sum += i
    print(f"Sum is {sum}")
else: print("Enter a valid number")

