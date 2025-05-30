# 🛠️ Mini Project: Number Guessing Game
# 1. Generate random number between 1–100
# 2. Ask user to guess until correct
# 3. Show "Too high" or "Too low" for wrong guesses
# 4. Track number of attempts

import random

# Define guess_number() function
def guess_number():
    secret_number = random.randint(1, 100)
    attempt = 0

    while True:
        attempt += 1
        if attempt % 10 == 1:
            print(f"\n {attempt}st attempt")
        elif attempt % 10 == 2:
            print(f"\n {attempt}nd attempt")
        elif attempt % 10 == 3:
            print(f"\n {attempt}rd attempt")
        else: print(f"\n {attempt}th attempt")

        user_input = int(input("Guess the number: "))
        if secret_number > user_input:
            print("Your number is too small")
        elif secret_number < user_input:
            print("Your number is too big")
        else: 
            print(f"Congratulations!!! You got it with {attempt} attempts")
            break

# Define main() function
def main():
    guess_number()


if __name__ == "__main__":
    main()


