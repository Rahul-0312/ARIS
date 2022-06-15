import os
from level3 import *
from level1 import *
from voice import speak
import sound


def level2(name, xp, shopping_points, item_list):
    print("========== LEVEL 2 ==========\n")
    speak("welcome to level-2\n")
    speak("""You are on your way, following the map to get to the treasure. You see your favourite celebrity, who wants to help you win this challenge and share the reward.\n""")
    speak("Do you want to pair up with them?")

    pair_choice = input("Yes (Y) or No (N) ").lower()

    if pair_choice == "yes" or pair_choice == "y":
        sound.play_game_over_wrongchoice()
        speak("\nUh Oh! You were killed by your favourite celebrity.\n")
        speak("You have 0 XP")
        sound.play_game_over()
        speak("Game over :( ")
        

    # Use line separators to get a better view of what's happening in terminal
    elif pair_choice == "no" or pair_choice == "n":
        xp += 20
        shopping_points+=20
        sound.play_correct_answer()
        speak("Good choice not pairing up! else you would have been killed!")    
        speak("You have been awarded a " + str(20) + " XP bonus and a " + str(20) + " shopping points bonus!")
        speak("Points left - " + str(shopping_points) + " points")
        speak("Your XP - " + str(xp) + " XP\n")
        sound.level_complete()
        print("==============================\n")
        speak("Good job - on to level 3\n")


        level3(name, xp, shopping_points, item_list)

# level2('raul', 70, 20, ['Gun', 'Sword', 'Medical Kit', 'Sword'])