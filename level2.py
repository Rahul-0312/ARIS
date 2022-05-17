import os
from level3 import *

def level2(name, xp, shopping_points, item_list):

    print("========== LEVEL 2 ==========")
    print("You are on your way following the map to the river that you need to "
          "cross to get the treasure and you see your favourite celebrity "
          "who wants to help you win this challenge and share the reward")
    print("Do you want to pair up with them? ")

    pair_choice = input("Yes (Y) or No (N) ")

    if pair_choice.lower().strip() == "yes" or pair_choice.lower().strip() == "y":
        print("Uh Oh! You were killed by your favourite celebrity")
        print("You have 0 XP")
        print("=================================")
        print("Game over :( ")

#Use line seperators to get a better view of what's happening in terminal
    elif pair_choice.lower().strip() == "no" or pair_choice.lower().strip() == "n":
        print("Good choice not pairing up or you would have been killed!")
        xp+= 20
        print("You have been given a " + str(20) + " XP bonus!")
        print("You now have - " + str(xp) + " XP")
        print("=================================")
        print("Good job - on to level 3")

        level3(name, xp, shopping_points, item_list)

