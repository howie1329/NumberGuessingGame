# GUESSING GAME
import random

CompNum = 0
PickNum = 0
Turns = 3
Wins = 0
Losses = 0
Play = True

# Heading
def Head():
    global Wins
    global Losses
    strwins = str(Wins)
    strlose = str(Losses)
    print("Game Won: " + strwins + " Games Lost: " + strlose)


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
    print(CompNum)


# Users Logic
def UsersTurn():
    global PickNum
    PickNum = int(input("Please pick a number between 1 - 20 "))
    print(PickNum)


def TurnsCheck():
    global Turns
    global Losses
    if Turns == 0:
        Losses = Losses + 1


# Number Check
def NumberCheck():
    global Turns
    global Play
    global CompNum
    global Losses
    global Wins
    while Turns > 1:
        if PickNum == CompNum:
            print("You Win")
            Wins = Wins + 1
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
    Head()
    TurnsCheck()


# Game Loop
while Play == True:
    print("Welcome to the Number Guessing Game")
    Menu()
    Head()
    UsersTurn()
    ComLogic()
    NumberCheck()
    Menu()
