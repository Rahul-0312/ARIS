import os
from level6 import *
from shopping import *
from voice import speak
import sound


def level5(name, xp, shopping_points, current_item_list):
    # print(name, xp, shopping_points)

    # create three chests
    print("========== BONUS LEVEL ==========\n")
    speak("Welcome to the bonus level.\nLet's see how lucky you are.\nYou are provided with three chests. Select "
          "amongst those three and take your rewards!\n")
    print("===========================\n")
    print("CHEST 1 |||| CHEST 2 ||||| CHEST 3")
    print("\n===========================\n")

    while (1):
        choice = input("1 or 2 or 3 : ")

        if choice == '1':
            shopping_points += 30
            print("\n===========================\n")
            sound.play_win_points()
            speak("Good Choice, you have 30 Shopping points added.")
            print("\n===========================\n")
            break
        elif choice == '2':
            shopping_points += 10
            print("\n===========================\n")
            sound.play_win_points()
            speak("Sorry, you only earned 10 Shopping points.")
            print("\n===========================\n")
            break
        elif choice == '3':
            shopping_points += 50
            print("\n===========================\n")
            sound.play_win_points()
            speak("Great Choice, you have 50 Shopping points added.")
            print("\n===========================\n")
            break
        else:
            print("\n===========================\n")
            speak("This choice is not available, please choose again!")
            print("\n===========================\n")

    speak("Well done on the bonus round. Hope you liked your reward. Let's go shop!\n")

    xp, shopping_points, item_list = shopping(xp, shopping_points)
    for item in current_item_list:
        item_list.append(item)

    inventory = dict()
    for item in item_list:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    speak("\nYour bag has "+' '.join([str(v) +"-"+ str(k)+". " for k,v in inventory.items()]))
    speak("Points left - " + str(shopping_points) + " points")
    speak("Your XP - " + str(xp) + " XP\n")
    print("\n===========================\n")
    sound.level_complete()
    level6(name, xp, shopping_points, item_list)

# level5('raul', 70, 20, ['Gun', 'Sword', 'Medical Kit', 'Sword'])
