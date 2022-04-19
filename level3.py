import os
from level4 import *
def level3(name, xp, shopping_points):
    
    print("========== LEVEL 3 ==========")
    print("=================================")
    print("Finally you are near the river bank. Find out a way to "
          "cross the river")
    print("Look around. You can see some options to cross the river. Choose wisely!")
    print("=================================")

    print("Option A - > There's an abandoned boat nearby. Might be an easy and quick way to cross the river")
    print("Option B - > There's a tree log. It might be useful in crossing the river")
    print("Option C - > Are you brave enough to swim across the river?")
    print("=================================")

    print("Choose your option! "
    "Hint : Two of the options takes you a bit closer to the treasure while the other one leads to 'DEATH'")

    choice = input("A, B or C  ")

    if choice == "A" or choice.lower().strip() == "a":
            print("Uh Oh! The boat had a hole. You drowned")
            print("You have 0 XP")
            print("=================================")
            print("Game over :( ")
    elif choice == "B" or choice.lower().strip() == "b":
            print("Good choice!")
            print("You have crossed the river now. You are 1 step ahead in your treasure hunt.")
            print("Also you've been rewarded extra 10XP for choosing the correct option")
            xp+=10
            print("Your current XP is now " + str(xp))
    elif choice == "C" or choice.lower().strip() == "c":
            print("Great choice!")
            print("You have crossed the river now. You are 1 step ahead in your treasure hunt.")
            print("Also you've been rewarded extra 20XP for your bravery!")
            xp+=20
            print("Your current XP is now " + str(xp))

            print("=================================")
            print("Good job - on to the next level now. Best of Luck! ")

            level4(name, xp, shopping_points)