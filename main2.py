import os
import fontstyle as fnt
import pyttsx3
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr
import smtplib
import random
from GuessGameV8_ import *
from superCalcy import *


# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('rate', 195)
# engine.setProperty('voice', voices[0].id)

# quickEngine = pyttsx3.init('sapi5')
# quickVoices = engine.getProperty('voices')
# quickEngine.setProperty('rate',230)
# quickEngine.setProperty('voice', voices[0].id)


def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 195)
    engine.setProperty('voice', voices[0].id)
    '''
    This function will speak or rather pronounce the argument which you will give it.
    '''
    engine.say(audio)
    engine.runAndWait()


def speakFast(audio):
    quickEngine = pyttsx3.init('sapi5')
    quickVoices = engine.getProperty('voices')
    quickEngine.setProperty('rate', 230)
    quickEngine.setProperty('voice', voices[0].id)
    '''
    This function will speak or rather pronounce the argument which you will give it. It it different from the speak funtion because this one speaks faster than the original speak funtnio.
    '''
    quickEngine.say(audio)
    quickEngine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
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
    print(fnt.apply('What\'s your name user?', 'blue/bold'))
    speak('What\'s your name, user?...')
    name = takeCommand()
    if name.lower() == 'krishna anand':
        name = 'Madhav'
        print(fontstyle.apply('Special user detected!', 'green/bold'))
        speak('Special user detected...')
    elif name.lower() == 'shivraj anand':
        name = 'Uncle SHIV'
        print(fnt.apply('I remember you are my uncle!...', 'yellow/bold'))
        speak('I remember you are my uncle!')
        print(fontstyle.apply('Special user detected!', 'green/bold'))
        speak('Special user detected...')
    elif 'shutdown' in name.lower() or 'bye' in name.lower():
        print(fontstyle.apply('Shutting down PARTH program...', 'red/bold'))
        speak('Shutting down PARTH program...')
        print(fontstyle.apply('Deactivated', 'red/bold'))
        exit()

    # assigns the current time in hours to a variable.
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print(fnt.apply(f'Good Morning {name}', 'blue/bold'))
        speak(f'Good Morning {name}...')

    elif hour >= 12 and hour < 18:
        print(fnt.apply(f'Good Afternoon {name}', 'blue/bold'))
        speak(f'Good Afternoon {name}...')

    elif hour == 12:
        print(fnt.apply(f'Good Noon {name}', 'blue/bold'))
        speak(f'Good Noon {name}...')

    else:
        print(fnt.apply(f'Good Evening {name}', 'blue/bold'))
        speak(f'Good Evening {name}...')

    print(fnt.apply('How may I help you?', 'blue/bold'))
    speak('How may I help you?')


def introduction():
    print(fnt.apply('Hi, It\'s PARTH!', 'cyan/bold'))
    speak('Hi, It\'s PARTH!')
    print(fnt.apply(
        'PARTH stands for Personal Artificial Rocking and Trustworthy Helper...', 'cyan/bold'))
    speak('PARTH stands for Personal Artificial Rocking and Trustworthy Helper...')
    print(fnt.apply(
        'I am an artificial intelligence programmed by Mr. Krishna Anand', 'cyan/bold'))
    speak('I am an artificial intelligence programmed by Mr. Krishna Anand')
    print('\n')
    print(fnt.apply('How may I help you?...'))
    speak('How may I help you?')


# if __name__ == '__main__':
#     print(fnt.apply('Initializing PARTH', 'blue/bold'))
#     speak('Initializing PARTH')
#     wishMe()


def main():
    while True:
        query = takeCommand().lower()
        '''This function defineslogic for excecuting task based on query'''

        if 'wikipedia' in query:
            print(fnt.apply('Searching Wikipedia', 'blue/bold'))
            speak('Searching Wikipedia')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=1)
            print(fnt.apply(results, 'blue/bold'))
            speak(results)

        elif 'essay' in query:
            print(fnt.apply('Searching Wikipedia', 'blue/bold'))
            speak('Searching Wikipedia')
            query = query.replace('long article', '')
            results = wikipedia.summary(query, sentences=10)
            print(fnt.apply(results, 'blue/bold'))
            speakFast(results)

        elif 'open youtube' in query:
            url = 'www.youtube.com'
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open google' in query.lower():
            url = 'www.google.com'
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open replit' in query.lower():
            url = 'https://replit.com/~'
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open web code' in query.lower():
            url = 'https://replit.com/~'
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open stack' in query.lower() and 'over' in query and 'flow' in query:
            url = 'stackoverflow.com'
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open whatsapp web' in query.lower():
            url = 'web.whatsapp.com'
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'play music' in query.lower():
            songs_dir = 'C:\\Users\\consu\\Desktop\\Krishna Super\\PARTH\\PARTH_music'
            songs = os.listdir(songs_dir)

            index = random.randint(0, len(songs)-1)
            os.startfile(os.path.join(songs_dir, songs[index]))

        elif 'search' and 'google' in query.lower():
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

            base_url = "http://www.google.com/search?q="

            print(fnt.apply('What should I search?', 'blue/bold'))
            speak('What should I search?')

            query = takeCommand()
            webbrowser.get(chrome_path).open_new(base_url+query)

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
                timeTxT = (fnt.apply(
                    f'{hourtime}:{mintime} p.m.', 'blue/bold'))
            elif hourtime == 12 and mintime > 0:
                time = (f'{hourtime} {mintime} p m...')
                timeTxT = (fnt.apply(
                    f'{hourtime}:{mintime} p.m.', 'blue/bold'))
            elif hourtime <= 12:
                time = (f'{hourtime} {mintime} a m...')
                timeTxT = (fnt.apply(
                    f'{hourtime}:{mintime} a.m.', 'blue/bold'))

            print(fnt.apply(strTime, 'blue/bold'))
            speak(f"The time is {strTime}")
            print(fnt.apply(timeTxT, 'blue/bold'))
            speak(f'It\'s {time}')

        elif 'open code' in query.lower():
            codePath = "C:\\external softwares\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'who am i' in query.lower():
            print(f'Your are my {name}')
            speak(f'Your are my {name}')

        elif 'maya' in query.lower():
            print(fontstyle.apply(
                f'M.A.Y.A. is like my elder sister. I used to call her didi.', 'yellow/bold/underline'))
            speak('MAYA is like my elder sister. I used to call her DI,DI...')

        elif 'clear' and 'screen' in query.lower():
            os.system('cls')
            print(fnt.apply('"Successfully cleared the screen"', 'green/bold'))
            speak('Successfully cleared the screen')

        elif 'introduce yourself' in query.lower():
            introduction()

        elif 'play' and 'game' in query.lower():
            os.system('cls')
            print(fontstyle.apply('Let\'s play a game!', 'blue/bold'))
            speak('Let\'s play a game...')
            print(fnt.apply('Choose your difficulty level.'))
            speak('Choose your difficulty level.')
            print(fnt.apply(
                'Enter 1 for easy mode, 2 for medium mode, 3 for hard mode and 4 for the impossible mode.', 'cyan/bold'))
            speak(
                ('Enter 1 for easy mode, 2 for medium mode, 3 for hard mode and 4 for the impossible mode.'))
            mode = int(input(fnt.apply('--->   ', 'blue/bold')))
            if mode == 1:
                print(fnt.apply('Downloading easy difficulty...', 'green/bold'))
                speak('Downloading easy difficulty...')
                main_game_(100)
            elif mode == 2:
                print(fnt.apply('Downloading medium difficulty...', 'yellow/bold'))
                speak('Downloading medium difficulty...')
                main_game_(250)
            elif mode == 3:
                print(fnt.apply('Downloading hard difficulty...', 'red/bold'))
                speak('Downloading hard difficulty...')
                main_game_(500)
            elif mode == 4:
                print(fnt.apply('Downloading impossible difficulty...', 'purple/bold'))
                speak('Downloading impossible difficulty...')
                main_game_(1000)
            elif mode == 5:
                print(fnt.apply('System Overloadd!\nDownloading Overload difficulty...', 'black/bold'))
                speak('System Overload! Downloading Overload difficulty...')
                main_game_(1000)
            else:
                print(fnt.apply('Can you please stop bothering me?', 'red/bold'))
                speak('Can you please stop bothering me?')

        elif 'open calculator' in query.lower():
            print(fnt.apply('Opening manual calculator...', 'blue/bold'))
            speak('Opening manual calculator...')
            main_calcy()

        elif 'change' in query.lower() and 'name' in query.lower():
            print(fnt.apply('Forgotting name...', 'blue/bold'))
            speak('Forgotting name...')
            print(fnt.apply('Tell me your name, user...', 'blue/bold'))
            speak('Tell me your name, user...')
            name = takeCommand()
            if name == 'Krishna Anand':
                name1 = 'Madhav'
                name = name1
            elif name == 'Shivraj Anand':
                name1 = 'Uncle Shiv'
                name = name1
                print(fnt.apply('I remember you are my uncle!...', 'yellow/bold'))
                speak('I remember you are my uncle!...')
            print(fnt.apply('Name changed succesfully', 'green/bold'))
            speak('Name changed succesfully')
            print(fnt.apply(f'Hi {name}', 'blue/bold'))
            speak(f'Hi {name}')

        elif 'repeat' in query.lower():
            print(fnt.apply(f'You said: {query}', 'blue/bold'))
            query = query.replace('repeat', '')
            speak(f'You said: {query}')

        elif 'shutdown' in query.lower():
            print(fontstyle.apply('Shutting down PARTH program...', 'red/bold'))
            speak('Shutting down PARTH program...')
            print(fontstyle.apply(f'Bye {name}', 'blue/bold'))
            speak(f'Bye {name}')
            print(fontstyle.apply('Deactivated', 'red/bold'))
            break

        else:
            print(fnt.apply('Command not recognised!', 'red/bold'))
            speak('Command not recognised!')


if __name__ == '__main__':
    os.system('cls')
    input(fnt.apply('Press ENTER to activate PARTH program: ', 'white/bold'))
    print(fnt.apply('Initializing PARTH', 'blue/bold'))
    speak('Initializing PARTH')
    wishMe()
    main()