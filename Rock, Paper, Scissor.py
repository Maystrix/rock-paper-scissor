
### ROCK, PAPER, SCISSOR ###

import random

# start condition
while True:
    choices = ['rock', 'paper', 'scissor']

    computer = random.choice(choices)          # computer input

    player = None                              # to handle wrong inputs and case senitivity

    while player not in choices:
        player = input("rock, paper, scissor ? :").lower()

    # checking result
    if player == computer:
        print("computer :", computer)
        print("player :", player)
        print("Tie !")

    elif player == "rock":
        if computer == 'paper':
            print("computer :", computer)
            print("player :", player)
            print("You Lose !")
        if computer == 'scissor':
            print("computer :", computer)
            print("player :", player)
            print("You Win !")

    elif player == "paper":
        if computer == 'scissor':
            print("computer :", computer)
            print("player :", player)
            print("You Lose !")
        if computer == 'rock':
            print("computer :", computer)
            print("player :", player)
            print("You Win !")

    elif player == "scissor":
        if computer == 'rock':
            print("computer :", computer)
            print("player :", player)
            print("You Lose !")
        if computer == 'paper':
            print("computer :", computer)
            print("player :", player)
            print("You Win !")

    # checking if player wants to continue or not
    play_again = input("Play Again (yes/no) ?:").lower()

    if play_again != 'yes':
        break
print("BYE !!!")