from level1 import *
import os
import sound

from level2 import level2

os.system('clear')  # clears the terminal before running the script

print("WELCOME TO ARIS")
print("=================================")
print("Do you want to play the game?")

while (1):

    response = input("Yes (Y) or No (N) ")
    name = ""
    xp = 50
    shopping_points = 100

    print("=================================")

    if response.lower().strip() == "yes" or response.lower().strip() == "y":
        print("Welcome to the game")
        print("=================================")
        name = input("Enter your name: ")
        print("Welcome to ARIS, " + name)

        # Level 1
        level1(name, xp, shopping_points)
        break

        # Level 2 is called from level 1 now




    elif response.lower().strip() == "no" or response.lower().strip() == "n":
        print("Goodbye")
        sound.play_game_over()
        break

    else:
        print("Please choose whether Yes/(Y) or No/(N)")
