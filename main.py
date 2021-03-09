from random import randint

playChoice = ["Rock", "Paper", "Scissors"]

computer = playChoice[randint(0, len(playChoice) - 1)]

player = False

while player == False:
    player = input("Rock, Paper, Scissors? > ")

    if player == computer:
        print("Tie")

    elif player == "Rock":
        if computer == "Paper":
            print("You lose,", computer, "beats", player)
        else:
            print("You win,", player, "beats", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose,", computer, "beats", player)
        else:
            print("You win,", player, "beats", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose,", computer, "beats", player)
        else:
            print("You win,", player, "beats", computer)

    else:
        print("That play is invalid, input is case-sensitive!")

    player = False
    computer = playChoice[randint(0, len(playChoice) - 1)]