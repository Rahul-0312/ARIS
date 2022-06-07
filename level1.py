import os
from level2 import *
from shopping import *
import sound


def level1(name, xp, shopping_points):
    print("========== LEVEL 1 ==========")
    xp, shopping_points, item_list = shopping(xp, shopping_points)
    sound.level_complete()
    level2(name, xp, shopping_points, item_list)

    #taking out name section from here and shifting it to main.py

   