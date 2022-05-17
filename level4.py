import os
from level5 import *

def level4(name, xp, shopping_points, item_list):
    monster_xp = 50

    print("========== LEVEL 4 ==========")
    print("=================================")
    print("A monster comes your way!!! Open your inventory and look for an item to defeat him.\n\n")
    print("Monster XP - ", str(monster_xp))
    print("""Each monster's hit will cost you 25 XP
    Hint:- Use Medic kit from the inventory to increase your XP by 50.""")
    friendly_itemlist = ', '.join(item_list)
    print("Your bag has - ", friendly_itemlist)
#We need item_list here in level 4
    while(1):
        print("Monster XP - ", str(monster_xp))
        print("Your XP - ", str(xp))
        
        #Your bag has - Medical Kit, Sword, Gun
        user_choice = input("Choose your weapon!\n M/S/G/B where M- Medical Kit, and so onnnnnnn\n").lower().strip()
        #Have an option to choose B&A even if we don't have it on our list
        if user_choice == "m" and "Medical Kit" in item_list:
            xp+=50
            item_list.remove("Medical Kit")
            print("You've increased your XP by 50 points")
            print("The items left in your bag are:-\n",item_list)
        elif user_choice=="s" and "Sword" in item_list:
            monster_xp-=25
            item_list.remove("Sword")
            print("You've hit the monster with a Sword")
            print("The items left in your bag are:-\n",item_list)
        elif user_choice=="g" and "Gun" in item_list:
            monster_xp-=50
            item_list.remove("Gun")
            print("You've hit the monster with a Gun")
            print("The items left in your bag are:-\n",item_list)
        elif user_choice=="b" and "Bow and Arrow" in item_list:
            monster_xp-=10
            item_list.remove("Bow and Arrow")
            print("You've hit the monster with a Bow and Arrow")
            print("The items left in your bag are:-\n",item_list)
        else:
            print("Wrong choice, please choose again!")

        if(monster_xp>0):
            print("Here comes the hit by the monster! Ahhhhh\n Your XP is reduced by 25")
            xp-=25
        else:
            break
    print("Well Done! You've defeated the monster!")
    print(name, xp, shopping_points)
    level5(name, xp, shopping_points)