import os
from level5 import *
from level1 import *
from voice import speak
import sound


def level4(name, xp, shopping_points, item_list):
    game_over = False

    def friendly_item_list(item_list):
        inventory = dict()
        for item in item_list:
            if item in inventory:
                inventory[item] += 1
            else:
                inventory[item] = 1
        speak("\nYour bag has " + ' '.join([str(v) + "-" + str(k) + ". " for k, v in inventory.items()]))
        # return ', '.join(item_list)

    monster_xp = 50

    print("========== LEVEL 4 ==========")
    speak("\nwelcome to level-4\n")
    sound.play_first_monster()
    speak("Uh Oh! A monster's coming in your way. Open your inventory and look for an item to defeat him.\n")
    # speak("Monster XP - " + str(monster_xp))
    speak(
        """Beware of the Monster's hit right after your hit. As it will reduce your XP by 25.\nHint:- Use Medical kit 
        from the inventory to increase your XP by 50.""")
    friendly_item_list(item_list)
    print("\n===========================\n")
    # We need item_list here in level 4
    while (1):

        speak("Monster XP is " + str(monster_xp))
        if xp <= 0:
            sound.play_player_dies()
            speak("Your XP is 0")
            speak("Uh oh! You're defeated by the monster! Better luck next time :(")
            sound.play_game_over()
            speak("Game Over :(")
            game_over = True
            break
        else:
            speak("Your XP is " + str(xp))

        # Your bag has Medical Kit, Sword, Gun
        speak("Choose your weapon!\n")
        user_choice = input(
            "M/m - Medical Kit or S/s - Sword or g/G - Gun or B/b - Bow & Arrow: ").lower().strip()
        # Have an option to choose B&A even if we don't have it on our list
        if user_choice == "m" and "Medical Kit" in item_list:
            xp += 50
            item_list.remove("Medical Kit")
            speak("You've increased your XP by 50")
            if len(item_list) != 0:
                friendly_item_list(item_list)
            print("\n===========================\n")
        elif user_choice == "s" and "Sword" in item_list:
            monster_xp -= 25
            item_list.remove("Sword")
            sound.play_sword_hit()
            speak("You've hit the monster with a Sword. Damage done - 25 xp")
            if len(item_list) != 0:
                friendly_item_list(item_list)
            print("\n===========================\n")
        elif user_choice == "g" and "Gun" in item_list:
            monster_xp -= 50
            item_list.remove("Gun")
            sound.play_gun_hit()
            speak("You've hit the monster with a Gun. Damage done - 50 xp")
            if len(item_list) != 0:
                friendly_item_list(item_list)
            print("\n===========================\n")
        elif user_choice == "b" and "Bow and Arrow" in item_list:
            monster_xp -= 10
            item_list.remove("Bow and Arrow")
            sound.play_bow_and_arrow_hit()
            speak("You've hit the monster with a Bow and Arrow. Damage done - 10 xp")
            if len(item_list) != 0:
                friendly_item_list(item_list)
            print("\n===========================\n")
        else:
            print("\n===========================\n")
            speak("This choice is not available")
            print("\n===========================\n")

        if monster_xp > 0:
            sound.play_first_monster_hit()
            speak("The monster hits you")
            speak("Your XP is reduced by 25")
            print("\n===========================\n")
            xp -= 25
        else:
            break

    if not game_over:
        xp += 20
        shopping_points += 10
        sound.play_monster_dies()
        speak("Well Done! You've defeated the monster! Take away your rewards - Extra 20 XP and 10 shopping points\n")
        sound.level_complete()
        level8(name, xp, shopping_points, item_list)

# level4('raul', 50, 20, ['Gun', 'Bow and Arrow', 'Medical Kit', 'Sword'])
