import os
from level4 import *
from level1 import *
from voice import speak
import sound


def level3(name, xp, shopping_points, item_list):
    print("========== LEVEL 3 ==========")
    speak("\nwelcome to level-3\n")
    speak("Oh! that's one fast flowing river. You need to find a way to cross this river.")
    speak("Look around. You can see some options to cross the river. Choose wisely!")
    print("\n==============================\n")

    speak("Option A - There's an abandoned boat nearby. Might be an easy and quick way to cross the river.")
    speak("Option B - There's a tree log. It might be useful in crossing the river.")
    speak("Option C - Are you brave enough to swim across the river?")
    print("\n==============================\n")

    speak("Choose your option!\nHint: Two of the options takes you closer to the treasure while the other one leads to DEATH!")

    choice = input("A, B or C\n").lower()

    if choice == "A" or choice == "a":
        sound.play_game_over_wrongchoice()
        speak("\nUh Oh! The boat had a hole. You drowned")
        speak("You have 0 XP")
        sound.play_game_over()
        speak("Game over :( ")

    elif choice == "B" or choice.lower().strip() == "b":
        sound.play_correct_answer()
        speak("\nGood Choice!\nYou have crossed the river now. You are 1 step ahead in your treasure hunt.")
        speak("Also you've been rewarded extra 10XP and 10 shopping points for choosing the correct option.")
        print("\n==============================\n")
        xp += 10
        shopping_points += 10
        speak("Points left - " + str(shopping_points) + " points")
        speak("Your XP - " + str(xp) + " XP\n")
        print("==============================\n")
        speak("Good job - on to level 4\n")
        sound.level_complete()
        level4(name, xp, shopping_points, item_list)

    elif choice == "C" or choice.lower().strip() == "c":
        sound.play_correct_answer()
        speak("\nGreat Choice!\nYou have crossed the river now. You are 1 step ahead in your treasure hunt.")
        speak("Also you've been rewarded extra 20XP and 20 shopping points for your bravery!")
        xp += 20
        shopping_points += 20
        speak("Points left - " + str(shopping_points) + " points")
        speak("Your XP - " + str(xp) + " XP\n")
        print("==============================\n")
        speak("Good job - on to level 4\n")
        sound.level_complete()
        level4(name, xp, shopping_points, item_list)

# level3('raul', 70, 20, ['Gun', 'Sword', 'Medical Kit', 'Sword'])