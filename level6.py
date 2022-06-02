import random
from level7 import *
from voice import speak

def level6(name, xp, shopping_points, item_list):
    print("========== LEVEL 6 ==========")
    speak("\nwelcome to level-6\n")
    riddles = {"What can run but never walk, has a mouth but never talks, has a head but never weeps, has a bed but never sleeps?":"River",
     "What is the capital in France":"F",
     "I have lakes with no water, mountains with no stone, and cities with no buildings. What am I?":"Map",
     "What begins with an “e” and only contains one letter?":"Envelope",
      }
    question = random.choice(list(riddles.keys()))
    speak(question)
    

    cnt = 3
    while(cnt>=1):
        user_answer = input("\n").lower()
        cnt-=1
        if(user_answer==riddles[question].lower()):
            speak("Correct Answer!\n")
            break
        else:
            print("\n===========================\n")
            speak("Wrong Answer! You have " + str(cnt) + " chances left")
            print("\n===========================\n")
    if(cnt==2):
        item_list.append("Gun")
        speak("Hurray! You got it at the first try, you got an extra Gun added to your inventory")
        print("\n===========================\n")
    elif(cnt==1):
        item_list.append("Sword")
        speak("Yippee! You got it at the second try, you got an extra Sword added to your inventory")
        print("\n===========================\n")
    elif(cnt==0):
        item_list.append("Bow and Arrow")
        item_list.append("Bow and Arrow")
        speak("Finally! You got it in the last try, you got two extra Bow and Arrows added to your inventory")
        print("\n===========================\n")

    # print(name, xp, shopping_points)
    level7(name, xp, shopping_points, item_list)
# level6('raul', 70, 20, ['Gun', 'Sword', 'Medical Kit', 'Sword'])