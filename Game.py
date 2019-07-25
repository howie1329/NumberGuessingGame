# Guessing Game
import random as r
import sys

# Global Var
wins = 0
losses = 0
play = ""
computer_number = 0
human_number = 0
turns = 0


# Heading
def heading():
    print("Welcome to Howard's Guessing Game")
    wins_loses()


# Menu
def menu():
    global play
    play = input("Would you like to play? (yes/no) ")
    if play.lower() == "yes":
        print("Lets get started")
        game_loop()
    else:
        print("Thanks for playing")
        sys.exit(0)


# Wins/Losses record
def wins_loses():
    print("Games Won: {} Games Losses: {}".format(wins, losses))


# Computer Logic
def computer_logic():
    global computer_number
    computer_number = r.randrange(0, 20)
    print("The Computer as picked a number.....")
    print("Debug-Computer_Number: {}".format(computer_number))


# User Logic
def user_logic():
    global human_number
    human_number = int(input("Pick a number between 0 - 20 "))


# number_logic
def number_logic():
    global play
    global wins
    if human_number == computer_number:
        print("You guessed the right number of {}".format(computer_number))
        wins += 1
        play = "no"
    elif human_number > computer_number:
        print("Your number of {} was larger then the computers number".format(human_number))
    elif human_number < computer_number:
        print("Your number of {} was smaller then the computers number".format(human_number))
    pass


# Turn Check
def turn_check():
    global turns
    global play
    global losses
    turns += 1
    if turns == 3 and human_number == computer_number:
        print("Game Over")
        play = "no"
    elif turns == 3:
        print("Game Over")
        losses += 1
        play = "no"


# GameLoop
def game_loop():
    computer_logic()
    while play.lower() == "yes":
        user_logic()
        number_logic()
        turn_check()
    wins_loses()
    menu()


# Game------------------
heading()
menu()
