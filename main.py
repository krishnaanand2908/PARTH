import os
import fontstyle
import pyttsx3
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr
import smtplib
import random
from GuessGameV8 import *

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
        
        print(fontstyle.apply(f'Good Morning {name}', 'blue/bold'))
        speak(f'Good Morning {name}...')
    elif hour >= 12 and hour < 18:
        
        print(fontstyle.apply(f'Good Afternoon {name}', 'blue/bold'))
        speak(f'Good Afternoon {name}...')
    elif hour == 12:
        
        print(fontstyle.apply(f'Good Noon {name}', 'blue/bold'))
        speak(f'Good Noon {name}...')
    else:
        
        print(fontstyle.apply(f'Good Evening {name}', 'blue/bold'))
        speak(f'Good Evening {name}...')
        


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

def introduction():
    print(fontstyle.apply('Hi, It\'s PARTH!', 'cyan/bold'))
    speak('Hi, It\'s PARTH!')
    print(fontstyle.apply('PARTH stands for Personal Artificial Rocking and Trustworthy Helper...', 'cyan/bold'))
    speak('PARTH stands for Personal Artificial Rocking and Trustworthy Helper...')
    print(fontstyle.apply('I am an artificial intelligence programmed by Mr. Krishna Anand', 'cyan/bold'))
    speak('I am an artificial intelligence programmed by Mr. Krishna Anand')
    print('\n')
    print(fontstyle.apply('How may I help you?...'))
    speak('How may I help you?')

def main():
    
    while(True):
    
        query = takeCommand()

        if 'wikipedia' in query.lower():
            print(fontstyle.apply('Searching it on web...', 'blue/bold'))
            speak('Searching it on WEB...')
            query = query.replace('wikipedia', '')
            try:
                results = wikipedia.summary(query, sentences = 3)
                print(fontstyle.apply(results, 'cyan/bold/underline'))
                speak(f'{results}...')
            except Exception as e:
                print(fontstyle.apply('An error occured! Please Try again', 'red/bold'))
                speak('An error occured... Please Try again...')
                continue
            
        elif 'clear' and 'screen' in query.lower():
            os.system('cls')
            print(fontstyle.apply('"Successfully cleared the screen"', 'green/bold'))
            speak('Successfully cleared the screen')
            
        elif 'introduce yourself' in query.lower():
            introduction()
            
        elif 'maya' in query.lower():
            print(fontstyle.apply(f'M.A.Y.A. is like my elder sister. I used to call her didi.', 'yellow/bold/underline'))
            speak('MAYA is like my elder sister. I used to call her di, di...')
            
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
                
        elif 'the time' in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            hourtime = int(datetime.datetime.now().hour)
            mintime = int(datetime.datetime.now().minute)
            time = None
            if hourtime == 0:
                hourtime == 24
                
            if hourtime > 12:
                hourtime = (hourtime - 12)
                time = (f'{hourtime} {mintime} p m...')
                timeTxT = (fontstyle.apply(f'{hourtime}:{mintime} p.m.', 'blue/bold'))
            elif hourtime == 12 and mintime > 0:
                time = (f'{hourtime} {mintime} p m...')
                timeTxT = (fontstyle.apply(f'{hourtime}:{mintime} p.m.', 'blue/bold'))
            elif hourtime <=12:
                time = (f'{hourtime} {mintime} a m...')
                timeTxT = (fontstyle.apply(f'{hourtime}:{mintime} a.m.', 'blue/bold'))
                
            
            
            print(fontstyle.apply(strTime, 'blue/bold'))
            speak(f"The time is {strTime}")
            print(fontstyle.apply(timeTxT, 'blue/bold'))
            speak(f'It\'s {time}')
            
        elif  'open code' in query.lower():
            codePath = "C:\\external softwares\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif 'shutdown' or 'bye' in query.lower():
            print(fontstyle.apply('Shutting down PARTH program...', 'red/bold'))
            speak('Shutting down PARTH program...')
            print(fontstyle.apply(f'Bye {name}', 'blue/bold'))
            speak(f'Bye {name}')
            print(fontstyle.apply('Deactivated', 'red/bold'))
            break
        
        elif 'who am i' in query.lower():
            print(f'Your name is {name}')
            speak(f'Your name is {name}')
            
        elif 'play' and 'game' in query.lower():
            os.system('cls')
            print(fontstyle.apply('Let\'s play a game!', 'blue/bold'))
            speak('Let\'s play a game...')
            main_game()
            
            

        else:
            
            speak(f'You said, {query}...')
            print(fontstyle.apply('Your command is not recognized!', 'red/bold'))
            speak('Your command is not recognized')
        
if __name__ == '__main__':
    os.system('cls')
    print(fontstyle.apply('Initializing PARTH...', 'blue/bold'))
    speak('Initializing PARTH...')
    print(fontstyle.apply('Activated', 'green/bold'))
    speak('Activated')
    print(fontstyle.apply('Tell me your name. ONLY NAME.', 'blue/bold'))
    speak('Tell me your name. ONLY NAME!!!...')
    name = takeCommand()
    if name.lower() == 'krishna anand' or name.lower() == 'k29':
        name = 'Madhav'
        print(fontstyle.apply('Special user detected!', 'green/bold'))
        speak('Special user detected...')
    elif name == 'shutdown' or name == 'bye':
        print(fontstyle.apply('Shutting down PARTH program...', 'red/bold'))
        speak('Shutting down PARTH program...')
        print(fontstyle.apply('Deactivated', 'red/bold'))
        exit()
    wishMe()
    print(fontstyle.apply('How may I help you?', 'blue/bold'))
    speak('How may I help you?...')
    main()
    
    
    
    