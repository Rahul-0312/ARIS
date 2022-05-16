import os
from level6 import *
from level1 import *

def level5(name, xp, shopping_points):

    print(name, xp, shopping_points)
    #create three chests

    [xp, shopping_points] = level1(name, xp, shopping_points)
    level6(name, xp, shopping_points)