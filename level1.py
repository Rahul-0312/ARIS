from level4 import level4
from shopping import *
from voice import speak
import sound


def level1(name, xp, shopping_points):
    print("========== LEVEL 1 ==========\n")
    speak("welcome to level-1\n")
    xp, shopping_points, item_list = shopping(xp, shopping_points)
    sound.level_complete()
    level4(name, xp, shopping_points, item_list)

    # taking out name section from here and shifting it to main.py
