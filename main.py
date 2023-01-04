import os
import fontstyle as fnt
import pyttsx3
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr
import random
from GuessGameV8_ import *
from superCalcy import *
import overloadgame


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
    date = f'{month}-{day}-{year}'

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
        print(fontstyle.apply('Special user detected!', 'green/bold'))
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

    print(fnt.apply(f"Hi, It's {program_name}!", 'cyan/bold'))
    speak(f"Hi, It's {program_name}!")
    print(
        fnt.apply(f"{program_name} stands for {program_full_form}", 'cyan/bold'))
    speak(f"{program_name} stands for {program_full_form}")

    print(
        fnt.apply(f'I am an artificial intellengence developed by {programmer}'))


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


def main():
    """This function defines the logic for executing tasks based on the query"""
    while True:

        query = takeCommand().lower()

        websites = {
            'youtube': 'www.youtube.com',
            'google': 'www.google.com',
            'replit': 'https://replit.com/~',
            'web code': 'https://replit.com/~',
            'stack overflow': 'stackoverflow.com',
            'whatsapp web': 'web.whatsapp.com',
            'chatGPT': 'chat.openai.com'
        }

        chrome_path = 'Google Chrome.lnk'

        praise_words = ['good', 'well done', 'very good',
                        'best', 'nice', 'amazing', 'excellent']
        not_good_words = ['worst', 'bad', 'worse',
                          'shut up', 'get lost', 'very bad', 'not good']

        for website, url in websites.items():
            if f'open {website}' in query.lower():
                print(fnt.apply(f'Opening {website}...', 'green/bold'))
                speak(f'Opening {website}')
                webbrowser.open(url)

        WIKI_SEARCH_OPTIONS = {'wikipedia': 1, 'essay': 10}

        if any(option in query for option in WIKI_SEARCH_OPTIONS):
            try:
                print(fnt.apply('Searching Wikipedia', 'blue/bold'))
                speak('Searching Wikipedia')
                # split query into words and unpack first and remaining words
                search_type, *search_query = query.split()
                num_sentences = WIKI_SEARCH_OPTIONS[search_type]
                # join remaining words into a single string
                results = wikipedia.summary(
                    ' '.join(search_query), sentences=num_sentences)
                print(fnt.apply(results, 'blue/bold'))
                speakFast(results)
            except:
                print(fnt.apply('An Error occured!', 'red/bold'))
                speak('An Error occured!')
                os.system('cls')

            # print(fnt.apply(f'Thank You {name}\n:)', 'yellow/bold/white_bg'))
            # speak(f'Thank You {name}\n:)')

        # elif query in praise_words:
        #     print(fnt.apply(f'I am really sorry {name}\n:(', 'yellow/bold/white_bg'))
        #     speak(f'I am really sorry {name}\n:(')

        elif 'play music' in query.lower():
            songs_dir = 'PARTH_music'
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

        elif 'open code' in query:
            codePath = "Visual Studio Code.lnk"
            os.startfile(codePath)

        elif 'who am i' in query or 'who i am' in query:
            print(f'Your are my {name}')
            speak(f'Your are my {name}')

        elif ('the date' or 'date') in query:
            print(fnt.apply(date, 'purple/bold'))
            speak(f'The date is {date}')

        elif 'maya' in query.lower():
            print(fontstyle.apply(
                f'M.A.Y.A. is like my elder sister. I used to call her didi.', 'yellow/bold/underline'))
            speak('MAYA is like my elder sister. I used to call her DI,DI...')

        elif 'clear' and 'screen' in query:
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
                'Enter 1 for easy mode, 2 for medium mode, 3 for hard mode, 4 for the impossible mode and 5 for the OVERLOAD difficulty!', 'cyan/bold'))
            speak(
                ('Enter 1 for easy mode 2 for medium mode 3 for hard mode 4 for the impossible mode and 5 for OVERLOAD difficulty!!!'))

            mode = (input(fnt.apply('--->   ', 'blue/bold')))

            if mode == "1":
                print(fnt.apply('Downloading easy difficulty...', 'green/bold'))
                speak('Downloading easy difficulty...')
                main_game_(100)
            elif mode == "2":
                print(fnt.apply('Downloading medium difficulty...', 'yellow/bold'))
                speak('Downloading medium difficulty...')
                main_game_(250)
            elif mode == "3":
                print(fnt.apply('Downloading hard difficulty...', 'red/bold'))
                speak('Downloading hard difficulty...')
                main_game_(500)
            elif mode == "4":
                print(fnt.apply('Downloading impossible difficulty...', 'purple/bold'))
                speak('Downloading impossible difficulty...')
                main_game_(1000)
            elif mode == "5":
                print(fnt.apply(
                    'System Overloadd!\nDownloading Overload difficulty...', 'black/bold'))
                speak('System Overload! Downloading Overload difficulty...')
                overloadgame.main_game_()
            else:
                print(fnt.apply('Can you please stop bothering me?', 'red/bold'))
                speak('Can you please stop bothering me?')
                print(fnt.apply('<(-_-)>/', 'red/bold'))

        elif 'open calculator' in query.lower():
            print(fnt.apply('Opening manual calculator...', 'blue/bold'))
            speak('Opening manual calculator...')
            main_calcy()

        elif 'change' in query.lower() and 'name' in query.lower():
            change_name()

        elif 'repeat' in query.lower():
            print(fnt.apply(f'{query}', 'blue/bold'))
            query = query.replace('repeat', '')
            speak(f'You said: {query}')

        elif 'shutdown' in query.lower() or 'bye' in query.lower():
            print(fontstyle.apply('Shutting down PARTH program...', 'red/bold'))
            speak('Shutting down PARTH program...')
            print(fontstyle.apply(f'Bye {name}', 'blue/bold'))
            speak(f'Bye {name}')
            print(fontstyle.apply('Deactivated', 'red/bold'))
            exit()
        
        else:
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
    wishMe()
    main()
