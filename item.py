import pyttsx3

voice_engine = pyttsx3.init()
voices = voice_engine.getProperty('voices')
voice_engine.setProperty('voice', voices[0].id)
# rate = voice_engine.getProperty('rate')   # getting details of current speaking rate                       #printing current voice rate
# voice_engine.setProperty('rate', 400) 

def speak(text):
    print(text)
    voice_engine.say(text)
    voice_engine.runAndWait()

# speak("The INVENTORY. \n"
#           + item_bag["item1"] + " - 15 points, \n"
#           + item_bag["item2"] + " - 25 points, \n"
#           + item_bag["item3"] + " - 30 points, \n"
#           + item_bag["item4"] + " - 20 points \n")

items = ['Gun', 'Sword', 'Medical Kit', 'Sword']

inventory = dict()
for item in items:
    if item in inventory:
        inventory[item] += 1
    else:
        inventory[item] = 1
items = ''.join([str(v) +"-"+ str(k)+". " for k,v in inventory.items()])
speak(items)
