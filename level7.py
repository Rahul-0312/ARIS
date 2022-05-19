import os
from level8 import *


def level7(name, xp, shopping_points, item_list):
    # print(name, xp, shopping_points)

    print("========== LEVEL 7 ==========")
    print("=================================")

    monster_xp = 100

    print("Another monster comes your way!!! Use everything you have in your inventory to defeat the monster!")
    print("Monster XP - ", str(monster_xp))
    print("Your XP - " + str(xp))
    print("""Each monster's hit will cost you 35 XP
        Hint:- Use Medic kit from the inventory to increase your XP by 50.""")

    # item_list.append("Gun")
    # item_list.append("Gun")
    # item_list.append("Bow and Arrow")

    friendly_itemlist = ', '.join(item_list)
    print("Your bag has - ", friendly_itemlist)

    print("Monster XP - ", str(monster_xp))
    print("Your XP - " + str(xp))

    # Your bag has - Medical Kit, Sword, Gun
    # user_choice = input("Choose your weapon!\n M/S/G/B where M- Medical Kit, and so onnnnnnn\n").lower().strip()

    while xp > 0:
        user_choice = input("Choose your weapon!\n M/S/G/B where M- Medical Kit, and so onnnnnnn\n").lower().strip()

        if user_choice == 'm' and "Medical Kit" in item_list:
            xp += 50
            item_list.remove("Medical Kit")
            print("You've increased your XP by 50 points")
            print("The items left in your bag are:-\n", friendly_list(item_list))
            print("Monster XP - ", str(monster_xp))
            print("Your XP - " + str(xp))

        elif user_choice == 's' and "Sword" in item_list:
            monster_xp -= 25
            item_list.remove("Sword")
            print("You've hit the monster with a Sword")
            print("The items left in your bag are:-\n", friendly_list(item_list))
            if monster_xp > 0:
                print("Here comes the hit by the monster! Ahhhhh\n Your XP is reduced by 25")
                xp -= 25
                print("Monster XP - ", str(monster_xp))
                print("Your XP - " + str(xp))
            else:
                break

        elif user_choice == 'g' and "Gun" in item_list:
            monster_xp -= 50
            item_list.remove("Gun")
            print("You've hit the monster with a Gun")
            print("The items left in your bag are:-\n", friendly_list(item_list))
            if monster_xp > 0:
                print("Here comes the hit by the monster! Ahhhhh\n Your XP is reduced by 25")
                xp -= 25
                print("Monster XP - ", str(monster_xp))
                print("Your XP - " + str(xp))
            else:
                break

        elif user_choice == 'b' and "Bow and Arrow" in item_list:
            monster_xp -= 10
            item_list.remove("Bow and Arrow")
            print("The items left in your bag are:-\n", friendly_list(item_list))
            print("You've hit the monster with a Bow and Arrow")
            if monster_xp > 0:
                print("Here comes the hit by the monster! Ahhhhh\n Your XP is reduced by 25")
                xp -= 25
                print("Monster XP - ", str(monster_xp))
                print("Your XP - " + str(xp))
            else:
                break

        else:
            print("The item you chose is not in your item bag. Please choose again")
            print("The items left in your bag are:-\n", friendly_list(item_list))

    if xp <= 0:
        print("THE MONSTER DEFEATED YOU! GAME OVER!")
    elif monster_xp <= 0:
        print("YOU HAVE DEFEATED THE MONSTER!")
        print("Good job - on to level 8")
        level8(name, xp, shopping_points, item_list)
    elif xp <= 0 and monster_xp <= 0:
        print("")
    else:
        level8(name, xp, shopping_points, item_list)


def friendly_list(itemlist):
    return ', '.join(itemlist)
