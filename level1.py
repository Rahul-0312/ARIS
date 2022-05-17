import os
from level2 import *

def level1(name, xp, shopping_points):

    name = input("Enter your name: ")
    print("Welcome to ARIS, " + name)


    print("You have " + str(xp) + " XP and " + str(shopping_points) + " points for shopping!")
    print("=================================")

#Take an argument to correctly display the level number
    print("========== LEVEL 1 ==========")
    print("Now, You have 100 points, choose items from the item list below that you will be taking with you on this challenge using those points")

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

    
    while shopping_points >= 15:
        
        print("Please choose an item you want: ")
        choice = input("A or B or C or D : ")
        if choice == "A" or choice.lower().strip() == "a":
            print("You chose " + item_bag["item1"])
            item_list.append(item_bag["item1"])
            shopping_points = shopping_points - 15
            print("You have " + str(shopping_points) + " points left ")
        elif choice == "B" or choice.lower().strip() == "b":
            if(shopping_points < 25):
                print("You don't have enough points to buy this")
            else:
                print("You chose " + item_bag["item2"])
                item_list.append(item_bag["item2"])
                shopping_points = shopping_points - 25
                print("You have " + str(shopping_points) + " points left ")
        elif choice == "C" or choice.lower().strip() == "c":
            if(shopping_points < 30):
                print("You don't have enough points to buy this")
            else:
                print("You chose " + item_bag["item3"])
                item_list.append(item_bag["item3"])
                shopping_points = shopping_points - 30
                print("You have " + str(shopping_points) + " points left ")
        elif choice == "D" or choice.lower().strip() == "d":
            if(shopping_points < 20):
                print("You don't have enough points to buy this")
            else:
                print("You chose " + item_bag["item4"])
                item_list.append(item_bag["item4"])
                shopping_points = shopping_points - 20
                print("You have " + str(shopping_points) + " points left ")
        else:
            print("Please enter a letter between A and D")

        print("=================================")

#friendly_itemlist - A dictionary should be implemented to have value as the no. of items and key to be the item itself.
    friendly_itemlist = ', '.join(item_list)
    print("Your bag has - " + friendly_itemlist) # user friendly format list
    print("Points left - " + str(shopping_points) + " points")
    print("XP - " + str(xp) + " XP")
    print("=================================")

    return xp, shopping_points, item_list


