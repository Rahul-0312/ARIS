import os
from level5 import *
from level1 import *
from voice import speak

def level4(name, xp, shopping_points, item_list):
    game_over = False
    def friendly_item_list(item_list):
        return ', '.join(item_list)
    monster_xp = 50

    print("========== LEVEL 4 ==========")
    speak("\nwelcome to level-4\n")
    speak("Uh Oh! A monster's coming in your way. Open your inventory and look for an item to defeat him.\n")
    speak("Monster XP - " + str(monster_xp))
    speak("""Beware of the Monster's hit right after your hit. As it will reduce your XP by 25.\nHint:- Use Medical kit from the inventory to increase your XP by 50.""")
    speak("Your bag has - " + str(friendly_item_list(item_list)))
    print("\n===========================\n")
    # We need item_list here in level 4
    while (1):
        
        speak("Monster XP - "+ str(monster_xp))
        if xp < 0:
            speak("Your XP - 0")
            speak("Uh oh! You're defeated by the monster! Better luck next time :(")
            speak("Game Over :(")
            game_over = True
            break
        else:
            speak("Your XP - " + str(xp))

        # Your bag has - Medical Kit, Sword, Gun
        user_choice = input("Choose your weapon!\nM/m - Medical Kit or S/s - Sword or g/G - Gun or B/b - Bow & Arrow: ").lower().strip()
        # Have an option to choose B&A even if we don't have it on our list
        if user_choice == "m" and "Medical Kit" in item_list:
            xp += 50
            item_list.remove("Medical Kit")
            speak("You've increased your XP by 50 points")
            speak("The items left in your bag are - " + str(friendly_item_list(item_list)))
            print("\n===========================\n")
        elif user_choice == "s" and "Sword" in item_list:
            monster_xp -= 25
            item_list.remove("Sword")
            speak("You've hit the monster with a Sword. Damage done - 25 xp")
            speak("The items left in your bag are - " + str(friendly_item_list(item_list)))
            print("\n===========================\n")
        elif user_choice == "g" and "Gun" in item_list:
            monster_xp -= 50
            item_list.remove("Gun")
            speak("You've hit the monster with a Gun. Damage done - 50 xp")
            speak("The items left in your bag are - " + str(friendly_item_list(item_list)))
            print("\n===========================\n")
        elif user_choice == "b" and "Bow and Arrow" in item_list:
            monster_xp -= 10
            item_list.remove("Bow and Arrow")
            speak("You've hit the monster with a Bow and Arrow. Damage done - 10 xp")
            speak("The items left in your bag are - " + str(friendly_item_list(item_list)))
            print("\n===========================\n")
        else:
            print("\n===========================\n")
            speak("This choice is not available, please choose again!")
            print("\n===========================\n")

        if monster_xp > 0:
            speak("Here comes the hit by the monster. Aahh!\nYour XP is reduced by 25")
            print("\n===========================\n")
            xp -= 25
        else:
            break
    
    if not game_over:
        xp+=20
        shopping_points+=10 
        speak("Well Done! You've defeated the monster! Take away your rewards - Extra 20 XP and 10 shopping points\n")
        level5(name, xp, shopping_points, item_list)

# level4('raul', 70, 20, ['Gun', 'Sword', 'Medical Kit', 'Sword'])