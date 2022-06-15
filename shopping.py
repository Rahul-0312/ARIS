from voice import speak
shopping_count = 1
def shopping(xp, shopping_points):
    global shopping_count

    speak("You have " + str(xp) + " XP and " + str(shopping_points) + " points for shopping!\n")
    print("=================================\n")

    
    speak(
        "Now, let's Shop. Choose items from the item list below, that you will be taking with you on this challenge using the shopping points.\n")

    item_bag = {
        "item1": "Medical Kit",
        "item2": "Sword",
        "item3": "Gun",
        "item4": "Bow and Arrow"
    }

    speak("The INVENTORY. \n"
          + item_bag["item1"] + " - 15 points, \n"
          + item_bag["item2"] + " - 25 points, \n"
          + item_bag["item3"] + " - 30 points, \n"
          + item_bag["item4"] + " - 20 points \n")
    print("==============================================\n")

    
    item_list = []

    while shopping_points >= 15:

        speak("Please choose an item you want: ")
        choice = input("M/m - Medical Kit or S/s - Sword or g/G - Gun or B/b - Bow & Arrow:").lower()
        if choice == "m":
            speak("You chose " + item_bag["item1"])
            item_list.append(item_bag["item1"])
            shopping_points = shopping_points - 15
            speak("You have " + str(shopping_points) + " points left ")
        elif choice == "s":
            if shopping_points < 25:
                speak("You don't have enough points to buy this")
            else:
                speak("You chose " + item_bag["item2"])
                item_list.append(item_bag["item2"])
                shopping_points = shopping_points - 25
                speak("You have " + str(shopping_points) + " points left ")
        elif choice == "g":
            if shopping_points < 30:
                speak("You don't have enough points to buy this")
            else:
                speak("You chose " + item_bag["item3"])
                item_list.append(item_bag["item3"])
                shopping_points = shopping_points - 30
                speak("You have " + str(shopping_points) + " points left ")
        elif choice == "b":
            if shopping_points < 20:
                speak("You don't have enough points to buy this")
            else:
                speak("You chose " + item_bag["item4"])
                item_list.append(item_bag["item4"])
                shopping_points = shopping_points - 20
                speak("You have " + str(shopping_points) + " points left ")
        else:
            speak("This choice is not available!")

        print("\n=================================\n")

    # friendly_itemlist - A dictionary should be implemented to have value as the no. of items and key to be the item itself.
    if shopping_count <= 1:
        inventory = dict()
        for item in item_list:
            if item in inventory:
                inventory[item] += 1
            else:
                inventory[item] = 1
        speak("\nYour bag has "+' '.join([str(v) +"-"+ str(k)+". " for k,v in inventory.items()]))
        speak("Points left - " + str(shopping_points) + " points")
        speak("Your XP - " + str(xp) + " XP\n")

    shopping_count += 1
    return xp, shopping_points, item_list
