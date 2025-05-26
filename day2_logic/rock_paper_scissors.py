#This program creates a rock-paper-scissors game between 2 players
valid = False
choices = ["rock", "paper", "scissors"]

while valid == False:
    player1_choice = input("Player 1 \nEnter your choice(rock, paper, scissors): ")
    if player1_choice in choices:
        valid = True
    else: print("Your input is not among the valid choices!")

valid = False
while valid == False:
    player2_choice = input("Player 2 \nEnter your choice(rock, paper, scissors): ")
    if player2_choice in choices:
        valid = True
    else: print("Your input is not among the valid choices!")

if player1_choice == player2_choice:
    print("You both enter the same thing. It's a tie!")
else:
    if player1_choice == "rock" and player2_choice == "scissors":
        print("Player1 wins")
    elif player1_choice == "scissors" and player2_choice == "paper":
        print("player1 wins")
    elif player1_choice == "paper" and player2_choice == "rock":
        print("Player1 wins")
    elif player1_choice == "scissors" and player2_choice == "rock":
        print("Player2 wins")
    elif player1_choice == "paper" and player2_choice == "scissors":
        print("player2 wins")
    elif player1_choice == "rock" and player2_choice == "paper":
        print("Player2 wins")
