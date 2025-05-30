# 4. sum_numbers.py
# - Ask user to enter numbers until they type "done"
# - Use while to keep summing the input

# Define sum_numbers() function
def sum_numbers():
    sum = 0
    user_input = input("Enter the numbers you want to sum: ")
    while user_input != "done":
        sum += int(user_input)
        user_input = input("Enter the next number: ")
    print(f"Sum is: {sum}")

# Define the main() function
def main():
    sum_numbers()

if __name__ == "__main__":
    main()