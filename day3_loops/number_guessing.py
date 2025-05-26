# 🎯 Mini Project: Number Guessing Game 🎯
# 🕹 Game Idea:
# - Program picks a number (e.g. 7)
# - User tries to guess it
# - Program gives hints: too low, too high, or correct

import random

picked_number = random.randint(1,10)

# Set number of trials to 3
counter = 3

while counter > 0:
    guess = input("Guess a number from 1 - 10: ")

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
        print("Game over! Try again.")
