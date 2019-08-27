# Guessing Game
import os
import random as r
import sys

# Global Var
wins = 0
losses = 0
play = ""
computer_number = 0
human_number = 0
turns = 3


# Heading
def heading():
    print("Welcome to Howard's Guessing Game")
    wins_loses()


# Menu
def menu():
    global play
    play = input("Would you like to play? (yes/no) ")
    if play.lower() == 'yes':
        print("Lets get started!!!")
        game_loop()
    elif play.lower() == 'no':
        print("Thanks for playing...")
        sys.exit(0)
    else:
        print('Wrong input please try again...')
        menu()


# Wins/Losses record
def wins_loses():
    print("Games Won: {} Games Losses: {}".format(wins, losses))


# Computer Logic
def computer_logic():
    global computer_number
    computer_number = r.randrange(0, 20)
    print("The Computer has picked a number.....")
    # print("Debug-Computer_Number: {}".format(computer_number))


# User Logic
def user_logic():
    global human_number
    print("You have {} turns left".format(turns))
    try:
        human_number = int(input("Pick a number between 0 - 20 "))
    except ValueError:
        print("Wrong number...")
        user_logic()
    else:
        if human_number > 20 or human_number < 0:
            print("Number higher then 20 or lower then 0")
            print("Try again....")
            user_logic()


# number_logic
def number_logic():
    global play
    global wins
    global turns
    if human_number == computer_number:
        print("You guessed the right number of {}".format(computer_number))
        wins += 1
        turns = 3
        play = "no"
    elif human_number > computer_number:
        print("Your number of {} was larger then the computers number".format(human_number))
    elif human_number < computer_number:
        print("Your number of {} was smaller then the computers number".format(human_number))


# Turn Check and computer number print
def turn_check():
    global turns
    global play
    global losses
    if human_number > computer_number or human_number < computer_number:
        turns -= 1
        if turns == 0 or turns <= 0:
            print('Better Luck Next Time...')
            print("The computer's number was {}".format(computer_number))
            turns = 3
            losses += 1
            play = 'no'


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
if __name__ == "__main__":
    heading()
    menu()
