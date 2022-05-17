from level1 import *
import os

from level2 import level2
os.system('clear') #clears the terminal before running the script

print("WELCOME TO ARIS")
print("=================================")
print("Do you want to play the game?")

response = input("Yes (Y) or No (N) ")
name = ""
xp = 50
shopping_points = 100


print("=================================")

if response.lower().strip() == "yes" or response.lower().strip() == "y":
    print("Welcome to the game")
    print("=================================")


    #Level 1
    [xp, shopping_points, item_list] = level1(name, xp, shopping_points)
   
    #Level 2
    level2(name, xp, shopping_points, item_list)
   


elif response.lower().strip() == "no" or response.lower().strip() == "n":
    print("Goodbye")

else:
    print("Please choose wether Yes/(Y) or No/(N)")
