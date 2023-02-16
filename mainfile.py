import os
import fontstyle as fnt
import pyttsx3
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr
import random
import GuessGameV8_
import superCalcy
import overloadgame
import pygame
import rps
import time

def speak(audio):
    '''
    This function will speak or rather pronounce the argument which you will give it.
    '''
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 198)
    engine.setProperty('voice', voices[0].id)

    engine.say(audio)
    engine.runAndWait()

def speakFast(audio):
    '''
    This function will speak or rather pronounce the argument which you will give it. It it different from the speak funtion because this one speaks faster than the original speak funtnio.
    '''
    quickEngine = pyttsx3.init('sapi5')
    quickVoices = quickEngine.getProperty('voices')
    quickEngine.setProperty('rate', 230)
    quickEngine.setProperty('voice', quickVoices[0].id)

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
        except:
            print(fnt.apply(f'Can\'t Recognize! Say that again please!', 'blue/bold'))
            return (fnt.apply('An error occured...', 'red/bold'))
    return query

def wishMe():
    '''
    This function will wish the user according to the current time if the device.
    '''

    day = int(datetime.datetime.now().day)  # defines day
    month = int(datetime.datetime.now().month)  # defines month
    year = int(datetime.datetime.now().year)  # defines year

    global date
    date = f'{day}-{month}-{year}'

    hour = int(datetime.datetime.now().hour)
    global name
    print(fnt.apply('What\'s your name user?', 'blue/bold'))
    speak('What\'s your name user?...')
    name = takeCommand()

    special_names = ["krishna anand", "shivraj anand"]

    if name.lower() in special_names:
        if name.lower() == special_names[0]:
            name = "Madhav"
        elif name.lower() == special_names[1]:
            name = "Uncle Shiv"
            print(fnt.apply("I remember you are my Uncle!", 'yellow/bold'))
            speak("I remember you are my Uncle!")
        print(fnt.apply('Special user detected!', 'green/bold'))
        speak('Special user detected...')

    if (hour >= 0 and hour < 12) or hour == 12:
        print(fnt.apply(f'Good Morning {name}', 'green/bold/underline'))
        speak(f'Good Morning {name}')
    elif (hour > 12 and hour < 18):
        print(fnt.apply(f'Good Afternoon {name}', 'green/bold/underline'))
        speak(f'Good Afternoon {name}')
    else:
        print(fnt.apply(f'Good Evening {name}', 'green/bold/underline'))
        speak(f'Good Evening {name}')
    if day == 1 and month == 1:
        print(fnt.apply(f"Happy New Year {name}", 'purple/bold/underline'))

    print(fnt.apply('How may I help you?', 'blue/bold'))
    speak('How may I help you?')
    
def introduction():
    program_name = "PARTH"
    program_full_form = "Personal Artificial Rocking and Trustworthy Helper"
    programmer = 'Mr. Krishna Anand'
    purpose = "To do various functions such as fast calculations, unit conversion, entertainment, provide information and to handle files."

    print(fnt.apply(f"Hi, It's {program_name}!", 'cyan/bold'))
    speak(f"Hi, It's {program_name}!")
    print(fnt.apply(f"{program_name} stands for {program_full_form}", 'cyan/bold'))
    speak(f"{program_name} stands for {program_full_form}")

    print(fnt.apply(f'I am an artificial intellengence developed by {programmer} {purpose}', ' cyan/bold'))
    speak(f'I am an artificial intellengence developed by {programmer} {purpose}')

def change_name():
    global name
    print(fnt.apply('Forgotting name...', 'blue/bold'))
    speak('Forgotting name...')
    print(fnt.apply('Tell me your name, user...', 'blue/bold'))
    speak('Tell me your name, user...')
    name = takeCommand()
    if not name or name.isspace():
        print(fnt.apply('Invalid name. Please try again.', 'red/bold'))
        speak('Invalid name. Please try again.')
        change_name()
    elif name == 'Krishna Anand':
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
    
def wikisearch(query):
    WIKI_SEARCH_OPTIONS = {'wikipedia': 1, 'essay': 10}
    if "wikipedia" in query:
        newquery = query.repace("wikipedia")
    else:
        newquery = query.replace("essay")
    for i in WIKI_SEARCH_OPTIONS.keys():
        if i in query:
            results = wikipedia.summary(newquery, sentences=WIKI_SEARCH_OPTIONS.get(i))
            break
    print(fnt.apply(results, "blue/bold"))
    speak(results) if i == "wikipedia" else speakFast(results)
    
def webOpen(query):
    global chrome_path
    websites = {
            'youtube': 'www.youtube.com',
            'google': 'www.google.com',
            'replit': 'https://replit.com/~',
            'web code': 'https://replit.com/~',
            'stack overflow': 'stackoverflow.com',
            'whatsapp web': 'web.whatsapp.com',
            'chatGPT': 'chat.openai.com'
        }
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    for website, url in websites.items():
        if f"open {website}" in query:
            print(fnt.apply(f"Opening {website}...", "green/bold"))
            speak(f"Opening {website}")
            webbrowser.open_new(url)
            
def webSearch():
    base_url = "https://www.google.com/search?q="
    print(fnt.apply("What should I search?", "blue/bold"))
    speak("What should I search?")
    content = takeCommand()
    webbrowser.open_new(base_url+content)
    
def playMusic(songsPath):
    songs = os.listdir(songsPath)
    index = random.randint(0, len(songs))
    os.startfile(songsPath, songs[index])
    
def openFile(filePath):
    os.startfile(filePath)
    
def whoAmI():
    print(f'Your are my {name}')
    speak(f'Your are my {name}')
    
def getDate():
    day = int(datetime.datetime.now().day)  # defines day
    month = int(datetime.datetime.now().month)  # defines month
    year = int(datetime.datetime.now().year)  # defines year

    global date
    date = f'{month}-{day}-{year}'
    print(fnt.apply(date, "purple/bold"))
    speak(date)
    
def gameing():
    gamelist = ["GuessTheNumber", "RockPaperScissors"]
    print(fnt.apply("What game do you want to play?", "blue/bold"))
    speak("What game do you want to play?")
    i = 1
    for game in gamelist:
        print(fnt.apply(f"{i} for {game}", "yellow/bold"))
        i=i+1
    gameChoice = int(input("--> "))
    os.system('cls')
    print(fnt.apply('Let\'s play a game!', 'blue/bold'))
    speak('Let\'s play a game...')
    match gameChoice:
        case 1:
            print(fnt.apply('Choose your difficulty level.'))
            speak('Choose your difficulty level.')
            print(fnt.apply(
                'Enter 1 for easy mode, 2 for medium mode, 3 for hard mode, 4 for the impossible mode and 5 for the OVERLOAD difficulty!', 'cyan/bold'))
            speak(
                ('Enter 1 for easy mode 2 for medium mode 3 for hard mode 4 for the impossible mode and 5 for OVERLOAD difficulty!!!'))
            mode = int((input(fnt.apply('--->   ', 'blue/bold'))))
            match mode:
                case 1:
                    print(fnt.apply('Downloading easy difficulty...', 'green/bold'))
                    speak('Downloading easy difficulty...')
                    GuessGameV8_.main(100)
                case 2:
                    print(fnt.apply('Downloading medium difficulty...', 'yellow/bold'))
                    speak('Downloading medium difficulty...')
                    GuessGameV8_.main(250)
                case 3:
                    print(fnt.apply('Downloading hard difficulty...', 'red/bold'))
                    speak('Downloading hard difficulty...')
                    GuessGameV8_.main(500)
                case 4:
                    print(fnt.apply(
                        'System Overloadd!\nDownloading Overload difficulty...', 'black/bold'))
                    speak('System Overload! Downloading Overload difficulty...')
                    overloadgame.main_game_()
                case _:
                    print(fnt.apply('Can you please stop bothering me?', 'red/bold'))
                    speak('Can you please stop bothering me?')
                    print(fnt.apply('<(-_-)>/', 'red/bold'))
        case 2:
            rps.RPS()
def openCalc():
    print(fnt.apply('Opening manual calculator...', 'blue/bold'))
    speak('Opening manual calculator...')
    superCalcy.main_calcy()
    
def repeat(query):
    print(fnt.apply(f'{query}', 'blue/bold'))
    query = query.replace('repeat', '')
    speak(f'You said: {query}')
    
def shutdown():
    print(fnt.apply('Shutting down PARTH program...', 'red/bold'))
    speak('Shutting down PARTH program...')
    print(fnt.apply(f'Bye {name}', 'blue/bold'))
    speak(f'Bye {name}')
    print(fnt.apply('Deactivated', 'red/bold'))
    exit()
    
def getTime():
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    print(fnt.apply(f"The time is {hour}:{minute}:{second}"))
    speak(f"The time is {hour} hours {minute} minutes and {second} seconds")
    if hour <= 12:
        if minute > 1:
            print(fnt.apply(f"It's {hour}:{minute} P.M."))
            speak(f"It's {hour}:{minute} P.M.")
        else:
            print(fnt.apply(f"It's {hour}:{minute} A.M."))
            speak(f"It's {hour}:{minute} A.M.")
    elif hour > 12:
        print(fnt.apply(f"It's {hour}:{minute} P.M."))
        speak(f"It's {hour}:{minute} P.M.")
    else:
        pass
    
def main():
    while True:
        query = takeCommand().lower()
        if "essay" in query or "wikipedia" in query:
            wikisearch(query)
            
        elif "open" in query:
            try:
                webOpen(query)
            except:
                openFile(query)
                
        elif "play music" in query:
            playMusic("PARTH_music")
            
        elif "search google" in query:
            webSearch(query)
            
        elif 'who am i' in query or 'who i am' in query:
            whoAmI()
        
        elif "maya" in query:
            print(fnt.apply(
                f'M.A.Y.A. is like my elder sister. I used to call her didi.', 'yellow/bold/underline'))
            speak('MAYA is like my elder sister. I used to call her DI,DI...')
            
        elif "clear" and "screen" in query:
            os.system('cls')
            print(fnt.apply('"Successfully cleared the screen"', 'green/bold'))
            speak('Successfully cleared the screen')
            time.sleep(2)
            os.system("cls")
            
        elif 'introduce yourself' in query:
            introduction()
            
        elif 'open calculator' in query:
            print(fnt.apply('Opening manual calculator...', 'blue/bold'))
            speak('Opening manual calculator...')
            superCalcy.main_calcy()
        
        elif 'change' in query.lower() and 'name' in query:
            change_name()
            
        elif "repeat" in query:
            repeat(query)
            
        elif "shutdown" in query or "bye" in query:
            print(fnt.apply('Shutting down PARTH program...', 'red/bold'))
            speak('Shutting down PARTH program...')
            print(fnt.apply(f'Bye {name}', 'blue/bold'))
            speak(f'Bye {name}')
            print(fnt.apply('Deactivated', 'red/bold'))
            exit()
            
        elif "the time" in query:
            getTime()
            
        elif "the date" in query or "date" in query:
            getDate()
        
        else:
            praise_words = ['good', 'well done', 'very good',
                        'best', 'nice', 'amazing', 'excellent']
            not_good_words = ['worst', 'bad', 'worse',
                          'shut up', 'get lost', 'very bad', 'not good']
            for x in praise_words:
                if x in query:
                    print(fnt.apply(f'Thank You {name}\n:)', 'yellow/bold/'))
                    speak(f'Thank You {name}\n:)')
                    break
            

            for y in not_good_words:
                if y in query: 
                    print(
                        fnt.apply(f'I am really sorry {name}\n:(', 'black/bold/'))
                    speak(f'I am really sorry {name}\n:(')
                    break

            if (x in query) or (y in query):
                pass
            elif 'give' in query:
                query = query.replace('give', '')
                print(fnt.apply(f'You give{query}', 'purple/bold'))
                speak(f'You give {query}')
            # if (x not in praise_words) or (y not in not_good_words):
            else:
                print(fnt.apply('Command not recognized!', 'red/bold'))
                speak('Command not recognized!')
        
if __name__ == '__main__':
    os.system('cls')
    input(fnt.apply('Press ENTER to activate PARTH program: ', 'white/bold'))
    os.system("cls")
    print(fnt.apply('Initializing PARTH', 'blue/bold'))
    speak('Initializing PARTH')
    # wishMe()
    name = "Krishna Anand"
    main()