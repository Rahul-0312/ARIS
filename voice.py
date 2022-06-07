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
