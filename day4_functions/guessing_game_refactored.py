# 💪 Bonus Task (Optional)
# Refactor your number guessing game from Day 3:
# Turn it into a function: def guessing_game():
# Call the function from main()


import random

def main():
    # Get the range from user
    range_list = get_range()

    # Get the secret number randomly using the limit from the user's input
    secret = random.randint(int(range_list[0]),int(range_list[1]))

    # Execute the guessing game
    guessing_game(range_list, secret)


"""get_range() function gets the user to input limit numbers 
to be used for the game to enhance flexibility of the game
and it return a list containing the range""" 

def get_range():
    number_range = input("Enter range e.g \"1-50\" or \"1-100\": ")
    range_list = number_range.split("-")
    return range_list


def guessing_game(range_list, secret):
    # Set number of trials to 3
    counter = 3

    while counter > 0:
        guess = input(f"Guess a number from {int(range_list[0])} - {int(range_list[1])}: ")

        if guess.isdigit():
            guess = int(guess)
            if guess > secret:
                print("Your number is too big")
            elif guess < secret:
                print("Your number is too small")
            else: 
                print("Wow! You are an alien")
                break
        else: print("Enter a valid number")
        counter -= 1

        if counter == 0:    # Check if number of trials is exceeded
            print(f"Game over! \n The secret number is {secret} \n Try again.")

# The code runs only if this file is executed directly
if __name__ == "__main__":
    main()
