# GUESSING GAME
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


# Computer

# Users Turn
def UsersTurn():
    PickNum = int(input('Please pick a number between 1 - 20 '))
    print(PickNum)

# Game Loop
while Play == True:
    print("Welcome to the Number Guessing Game")
    Menu()
    UsersTurn()
    Menu()
