import os
import random
from level7 import *
import sound


def level6(name, xp, shopping_points, item_list):
    riddles = {
        "What can run but never walks, has a mouth but never talks, has a head but never weeps, has a bed but never sleeps?": "River",
        "What is the capital in France": "F",
        "I have lakes with no water, mountains with no stone, and cities with no buildings. What am I?": "Map",
        "What begins with an “e” and only contains one letter?": "Envelope",
        }
    question = random.choice(list(riddles.keys()))
    print(question)

    cnt = 3
    while (cnt >= 1):
        user_answer = input("\n").lower()
        cnt -= 1
        if (user_answer == riddles[question].lower()):
            print("Correct Answer!\n")
            sound.play_correct_answer()
            break
        else:
            print("Wrong Answer! You have " + str(cnt) + " chances left")
            sound.play_wrong_answer()

    if (cnt == 2):
        item_list.append("Gun")
        print("Hurray! You got it at the first try, you got an extra Gun added to your inventory")
        sound.play_win_points()
    elif (cnt == 1):
        item_list.append("Sword")
        print("Yippee! You got it at the second try, you got an extra Sword added to your inventory")
        sound.play_win_points()
    elif (cnt == 0):
        item_list.append("Bow and Arrow")
        item_list.append("Bow and Arrow")
        sound.play_win_points()
        print("Finally! You got it in the last try, you got two extra Bow and Arrows added to your inventory")

    # print(name, xp, shopping_points)
    sound.level_complete()
    level7(name, xp, shopping_points, item_list)
