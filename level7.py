from level8 import *
from voice import speak
import sound


# Let's brainstorm on this if we have time

def level7(name, xp, shopping_points, item_list):
    game_over = False

    def friendly_item_list(item_list):
        inventory = dict()
        for item in item_list:
            if item in inventory:
                inventory[item] += 1
            else:
                inventory[item] = 1
        speak("\nYour bag has "+' '.join([str(v) +"-"+ str(k)+". " for k,v in inventory.items()]))

    print("========== LEVEL 7 ==========")
    speak("\nwelcome to level-7\n")
    monster_xp = 100

    sound.play_second_monster()
    speak("Another monster comes your way!!! Use everything you have in your inventory to defeat the monster!")
    speak("""Beware of the Monster's hit right after your hit. As it will reduce your XP by 35.\nHint:- Use Medical kit from the inventory to increase your XP by 50.""")

    # item_list.append("Gun")
    # item_list.append("Gun")
    # item_list.append("Bow and Arrow")

    friendly_item_list(item_list)
    print("\n===========================\n")

    # Your bag has Medical Kit, Sword, Gun
    # user_choice = input("Choose your weapon!\n M/S/G/B where M- Medical Kit, and so onnnnnnn\n").lower().strip()

    while (1):

        speak("The Monster's XP is " + str(monster_xp))
        if xp <= 0:
            sound.play_player_dies()
            speak("Your XP is 0")
            speak("Uh oh! You're defeated by the monster")
            speak("Game Over :(")
            game_over = True
            sound.play_game_over()
            break
        else:
            speak("Your XP is " + str(xp))

        # Your bag has Medical Kit, Sword, Gun
        user_choice = input(
            "Choose your weapon!\nM/m - Medical Kit or S/s - Sword or g/G - Gun or B/b - Bow & Arrow: ").lower().strip()
        # Have an option to choose B&A even if we don't have it on our list
        if user_choice == "m" and "Medical Kit" in item_list:
            xp += 50
            item_list.remove("Medical Kit")
            speak("You've increased your XP by 50 points")
            friendly_item_list(item_list)
            print("\n===========================\n")
        elif user_choice == "s" and "Sword" in item_list:
            monster_xp -= 25
            item_list.remove("Sword")
            sound.play_sword_hit()
            speak("You've hit the monster with a Sword. Damage done - 25xp")
            friendly_item_list(item_list)
            print("\n===========================\n")
        elif user_choice == "g" and "Gun" in item_list:
            monster_xp -= 50
            item_list.remove("Gun")
            sound.play_gun_hit()
            speak("You've hit the monster with a Gun. Damage done - 50xp")
            friendly_item_list(item_list)
            print("\n===========================\n")
        elif user_choice == "b" and "Bow and Arrow" in item_list:
            monster_xp -= 10
            item_list.remove("Bow and Arrow")
            sound.play_bow_and_arrow_hit()
            speak("You've hit the monster with a Bow and Arrow. Damage done - 10xp")
            friendly_item_list(item_list)
            print("\n===========================\n")
        else:
            print("\n===========================\n")
            speak("This choice is not available.")
            print("\n===========================\n")

        if monster_xp > 0:
            sound.play_second_monster_hit()
            speak("The monster hits you")
            speak("Your XP is reduced by 25")
            print("\n===========================\n")
            xp -= 35
        else:
            break
    if not game_over:
        #monster dead sound
        sound.play_monster_dies()
        speak("Well Done! You've defeated the monster. Onto the last level\n")
        sound.level_complete()
        level8(name, xp, shopping_points, item_list)

    # while xp > 0:
    #     user_choice = input("Choose your weapon!\nM/m - Medical Kit or S/s - Sword or g/G - Gun or B/b - Bow & Arrow: ").lower().strip()

    #     if user_choice == 'm' and "Medical Kit" in item_list:
    #         xp += 50
    #         item_list.remove("Medical Kit")
    #         speak("You've increased your XP by 50 points")
    #         speak("The items left in your bag are - " + str(friendly_list(item_list)))
    #         speak("Monster XP - "+ str(monster_xp))
    #         speak("Your XP - " + str(xp))

    #     elif user_choice == 's' and "Sword" in item_list:
    #         monster_xp -= 25
    #         item_list.remove("Sword")
    #         speak("You've hit the monster with a Sword")
    #         speak("The items left in your bag are - "+ str(friendly_list(item_list)))
    #         if monster_xp > 0:
    #             speak("Here comes the hit by the monster! Ahhhhh\n Your XP is reduced by 25")
    #             xp -= 25
    #             speak("Monster XP - "+ str(monster_xp))
    #             speak("Your XP - " + str(xp))
    #         else:
    #             break

    #     elif user_choice == 'g' and "Gun" in item_list:
    #         monster_xp -= 50
    #         item_list.remove("Gun")
    #         speak("You've hit the monster with a Gun")
    #         speak("The items left in your bag are - "+ str(friendly_list(item_list)))
    #         if monster_xp > 0:
    #             speak("Here comes the hit by the monster! Ahhhhh\n Your XP is reduced by 25")
    #             xp -= 25
    #             speak("Monster XP - "+ str(monster_xp))
    #             speak("Your XP - " + str(xp))
    #         else:
    #             break

    #     elif user_choice == 'b' and "Bow and Arrow" in item_list:
    #         monster_xp -= 10
    #         item_list.remove("Bow and Arrow")
    #         speak("The items left in your bag are - "+ str(friendly_list(item_list)))
    #         speak("You've hit the monster with a Bow and Arrow")
    #         if monster_xp > 0:
    #             speak("Here comes the hit by the monster! Aahh\n Your XP is reduced by 25")
    #             xp -= 25
    #             speak("Monster XP - "+ str(monster_xp))
    #             speak("Your XP - " + str(xp))
    #         else:
    #             break

    #     else:
    #         speak("The item you chose is not in your item bag. Please choose again")
    #         speak("The items left in your bag are - "+ str(friendly_list(item_list)))

    # if xp <= 0:
    #     speak("THE MONSTER DEFEATED YOU! GAME OVER!")
    # elif monster_xp <= 0:
    #     speak("YOU HAVE DEFEATED THE MONSTER!")
    #     speak("Good job - on to level 8")
    #     level8(name, xp, shopping_points, item_list)
    # elif xp <= 0 and monster_xp <= 0:
    #     print("")
    # else:

# level7('raul', 10, 20, ['Gun', 'Sword', 'Medical Kit', 'Sword'])
