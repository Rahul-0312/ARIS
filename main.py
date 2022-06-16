from level1 import *
import os
import sound
from level2 import level2
from voice import speak

os.system('clear')  # clears the terminal before running the script

speak("WELCOME TO ARIS")
sound.aris_intro()
print("=================================\n")
speak("Do you want to play the game?")

while 1:
    speak("If Yes enter (Yes or y) else No (No or n)")
    response = input()
    name = ""
    xp = 50
    shopping_points = 100

    print("\n=================================\n")

    if response.lower().strip() == "yes" or response.lower().strip() == "y":
        speak("Welcome to the game")
        print("\n=================================\n")
        speak("Enter your name: ")
        name = input()
        speak("\nWelcome to ARIS, " + name + "!\n")

        # Level 1
        level1(name, xp, shopping_points)
        break

        # Level 2 is called from level 1 now




    elif response.lower().strip() == "no" or response.lower().strip() == "n":

        speak("Goodbye")
        sound.play_game_over()
        break

    else:
        speak("Please choose right option!")
