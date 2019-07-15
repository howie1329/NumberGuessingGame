# GUESSING GAME
import random

CompNum = 0
PickNum = 0
Turns = 3
Play = True


# Menu
def Menu():
    global Play
    choice = input("Would you like to play? (yes/no) ")
    if choice == "no":
        print("Thanks for Playing")
        Play = False
    else:
        print("Lets get started!!!")
        Play = True


# Computer Logic
def ComLogic():
    global CompNum
    CompNum = random.randrange(0, 20)


# Users Logic
def UsersTurn():
    global PickNum
    PickNum = int(input("Please pick a number between 1 - 20 "))
    print(PickNum)


# Number Check
def NumberCheck():
    global Turns
    global Play
    global CompNum
    while Turns > 0:
        if PickNum == CompNum:
            print("You Win")
            Play = False
            Turns = 0
            break
        elif PickNum > CompNum:
            print("Your number was higher then the guess")
            print("Try Again")
            Turns = Turns - 1
            UsersTurn()
        elif PickNum < CompNum:
            print("Your number was lower then the guess")
            print("Try Again")
            Turns = Turns - 1
            UsersTurn()


# Game Loop
while Play == True:
    print("Welcome to the Number Guessing Game")
    Menu()
    UsersTurn()
    ComLogic()
    NumberCheck()
    Menu()
