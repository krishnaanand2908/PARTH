import os
import fontstyle
import pyttsx3
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr
import smtplib
import random

engine = pyttsx3.init('sapi5') # initializes sapi5 which is a voice api developed by Microsoft itself.
voices = engine.getProperty('voices') #gets the properties of all the available vocies.
engine.setProperty('voice', voices[0].id) # sets the given voice in the program.


# speak function will speak/pronounce the which string which is passed to it.
def speak(text):
    engine.say(text)
    engine.runAndWait()

# wishMe function will use datetime module and will greet the user according to the current time of your device.  
def wishMe():
    hour = int(datetime.datetime.now().hour) # assigns the current time in hours to a variable.
    if hour >= 0 and hour < 12:
        speak('Good Morning...')
        print(fontstyle.apply('Good Morning'))
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon...')
        print(fontstyle.apply('Good Afternoon'))
    elif hour == 12:
        speak('Good Noon...')
        print(fontstyle.apply('Good Noon'))
    else:
        speak('Good Evening...')
        print(fontstyle.apply('Good Evening'))

# takeCommand function will take input from the user in the form of voice.   
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(fontstyle.apply('Listening...', 'blue/bold'))
        audio = r.listen(source)
        
    try:
        print(fontstyle.apply('Recognizing...', 'blue/bold'))
        query = r.recognize_google(audio, language = 'en-in')
        print(fontstyle.apply(f'User said: {query}\n', 'blue/bold'))
    except Exception as e:
        print(fontstyle.apply('Can\'t recognize! Say that again please', 'blue/bold'))
    return query  


query = takeCommand()

if 'wikipedia' in query.lower():
    print(fontstyle.apply('Searching it on web...', 'blue/bold'))
    speak('Searching it on WEB...')
    query = query.replace('wikipedia', '')
    results = wikipedia.summary(query, sentences = 3)
    print(fontstyle.apply(results, 'cyan/bold/underline'))
    speak(f'{results}...')
    
elif 'open youtube' in query.lower():
    url = 'www.youtube.com'
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    
elif 'open google' in query.lower():
    url = 'www.google.com'
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    
elif 'open replit'  in query.lower():
    url = 'https://replit.com/~'
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    
elif 'open stackoverflow' in query.lower():
    url = 'www.stackoverflow.com'
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    
elif 'open whatsapp web' in query.lower():
    url = 'web.whatsapp.com'
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    
    
elif 'play music' in query.lower():
    songs_dir = 'C:\\Users\\consu\\Desktop\\Krishna Super\\PARTH\\PARTH_music'
    songs = os.listdir(songs_dir)
    print(songs)
    # os.startfile(os.path.join(songs_dir, songs[0]))
  
    a = random.randint(1, 3)
    if a == 1:
        os.startfile(os.path.join(songs_dir, songs[0]))
    else:
        os.startfile(os.path.join(songs_dir, songs[1]))
else:
    print()