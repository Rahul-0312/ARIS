import os
from level2 import *

def level1(name, xp, shopping_points):

    name = input("Enter your name: ")
    print("Welcome to ARIS, " + name)


    print("You have " + str(xp) + " XP and " + str(shopping_points) + " points for shopping!")
    print("=================================")


    print("========== LEVEL 1 ==========")
    print("Now, choose 3 items from the item list below that you will be taking with you on this challenge")

    item_bag = {
        "item1" : "Medical Kit",
        "item2" : "Sword",
        "item3" : "Gun",
        "item4" : "Bow and Arrow"
    }

    print("INVENTORY: \n"
          + item_bag["item1"] + " - 15 points \n"
          + item_bag["item2"] + " - 25 points \n"
          + item_bag["item3"] + " - 30 points \n"
          + item_bag["item4"] + " - 20 points")
    print("==============================================")

    item_list = []

    
    choice_count = 0
    while choice_count < 3:
        
        print("Please choose an item you want: ")
        choice = input("A or B or C or D : ")
        if choice == "A" or choice.lower().strip() == "a":
            print("You chose " + item_bag["item1"])
            item_list.append(item_bag["item1"])
            shopping_points = shopping_points - 15
            print("You have " + str(shopping_points) + " points left ")
        elif choice == "B" or choice.lower().strip() == "b":
            print("You chose " + item_bag["item2"])
            item_list.append(item_bag["item2"])
            shopping_points = shopping_points - 25
            print("You have " + str(shopping_points) + " points left ")
        elif choice == "C" or choice.lower().strip() == "c":
            print("You chose " + item_bag["item3"])
            item_list.append(item_bag["item3"])
            shopping_points = shopping_points - 30
            print("You have " + str(shopping_points) + " points left ")
        elif choice == "D" or choice.lower().strip() == "d":
            print("You chose " + item_bag["item4"])
            item_list.append(item_bag["item4"])
            shopping_points = shopping_points - 20
            print("You have " + str(shopping_points) + " points left ")
        else:
            print("Please enter a letter between A and D")
            choice_count -= 1

        print("=================================")
        choice_count += 1

    friendly_itemlist = ', '.join(item_list)
    print("Your bag has - " + friendly_itemlist) # user friendly format list
    print("Points - " + str(shopping_points) + " points")
    print("XP - " + str(xp) + " XP")
    print("=================================")

    return xp, shopping_points


