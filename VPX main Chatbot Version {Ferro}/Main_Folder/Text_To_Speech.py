#Librarys {Public}

import pyttsx3

#Functions

def speak(text, volume=0.8, rate=150):
    engine = pyttsx3.init()
    engine.setProperty('volume', volume)
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()