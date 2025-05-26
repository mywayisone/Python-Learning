# 🧠 Optional Challenge
# Let the user choose the difficulty by picking the range (e.g. 1–50 or 1–100), 
# and use random.randint() to generate the secret number.

import random

number_range = input("Enter range e.g \"1-50\" or \"1-100\": ")
range_list = number_range.split("-")

picked_number = random.randint(int(range_list[0]),int(range_list[1]))

# Set number of trials to 3
counter = 3

while counter > 0:
    guess = input(f"Guess a number from {int(range_list[0])} - {int(range_list[1])}: ")

    if guess.isdigit():
        guess = int(guess)
        if guess > picked_number:
            print("Your number is too big")
        elif guess < picked_number:
            print("Your number is too small")
        else: 
            print("Wow! You are an alien")
            break
    else: print("Enter a valid number")
    counter -= 1

    if counter == 0:    # Check if number of trials is exceeded
        print(f"Game over! \n The secret number is {picked_number} \n Try again.")
