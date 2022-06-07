import os
from level6 import *
from shopping import *
import sound


def level5(name, xp, shopping_points, current_item_list):
    # print(name, xp, shopping_points)
    # create three chests
    print("========== BONUS LEVEL ==========")
    print(
        "Welcome to the bonus leveL\nLet's see how lucky you are!\nYou are provided with three chests.Select amongst those three and take your rewards!!!")
    print(" CHEST 1 |||| CHEST 2 ||||| CHEST 3")

    while (1):
        choice = input("1 or 2 or 3 : ")
        if choice == '1':
            shopping_points += 30
            sound.play_win_points()
            break
        elif choice == '2':
            shopping_points += 10
            sound.play_win_points()
            break
        elif choice == '3':
            shopping_points += 50
            sound.play_win_points()
            break
        else:
            print("This choice is not available, please choose again!")

    print("Well done on the bonus round. hope you liked your reward. Let's go for shopping :)\n\n")

    xp, shopping_points, item_list = shopping(xp, shopping_points)
    for item in current_item_list:
        item_list.append(item)
    sound.level_complete()
    level6(name, xp, shopping_points, item_list)
