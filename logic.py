import os
import fontstyle as fnt
import pyttsx3
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr
import random
from GuessGameV8_easy import *
from GuessGameV8_hard import *
from GuessGameV8_medium import *
from GuessGameV8_impossible import *
from superCalcy import *


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 195)
engine.setProperty('voice', voices[0].id)

quickEngine = pyttsx3.init('sapi5')
quickVoices = engine.getProperty('voices')
quickEngine.setProperty('rate', 230)
quickEngine.setProperty('voice', voices[0].id)


def speak(audio):
    '''
    This function will speak or rather pronounce the argument which you will give it.
    '''
    engine.say(audio)
    engine.runAndWait()


def speakFast(audio):
    '''
    This function will speak or rather pronounce the argument which you will give it. It it different from the speak funtion because this one speaks faster than the original speak funtnio.
    '''
    quickEngine.say(audio)
    quickEngine.runAndWait()


r = sr.Recognizer()


def takeCommand():
    with sr.Microphone() as source:
        print(fnt.apply('Listening...', 'blue/bold'))
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
        try:
            print(fnt.apply('Recognizing...', 'blue/bold'))
            query = r.recognize_google(audio, language='en-in')
            print(fnt.apply(f'User said: {query}', 'blue/bold'))
        except Exception as e:
            print(fnt.apply(f'Can\'t Recognize! Say that again please!', 'blue/bold'))
            return (fnt.apply('An error occured...', 'red/bold'))
    return query


def wishMe():
    '''
    This function will wish the user according to the current time if the device.
    '''
    hour = int(datetime.datetime.now().hour)
    name = takeCommand()
    name_lower = name.lower()
    greetings = {
        0: "Good Morning",
        12: "Good Noon",
        18: "Good Afternoon",
    }
    # Use the "hour" variable to get the greeting message
    greeting = greetings.get(hour, "Good Evening")

    
    
    special_names = ["krishna anand", "shivraj anand"]

    # Check if the user's name is in the list of special names
    if name_lower in special_names:
        # Use the name mapping to get the special name
        name_mapping = {"krishna anand": "Madhav", "shivraj anand": "Uncle SHIV"}
        name = name_mapping[name_lower]
        
        print(fontstyle.apply('Special user detected!', 'green/bold'))
        speak('Special user detected...')
        
     # Use the greeting message to greet the user
    print(fnt.apply(f'{greeting} {name}', 'blue/bold'))
    speak(f'{greeting} {name}...')
    

def introduction():
    program_name = "PARTH"
    program_full_form = "Personal Artificial Rocking and Trustworthy Helper"
    programmer = 'Mr. Krishna Anand'

    print(fnt.apply(f"Hi, It's {program_name}!", 'cyan/bold'))
    speak(f"Hi, It's {program_name}!")
    print(fnt.apply(f"{program_name} stands for {program_full_form}", 'cyan/bold'))
    speak(f"{program_name} stands for {program_full_form}")
    
    print(fnt.apply(f'I am an artificial intellengence developed by {programmer}'))
    


def main():
    pass

