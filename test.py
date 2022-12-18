import webbrowser
import pyttsx3
import pyaudio
import fontstyle
import speech_recognition as sr

# chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

# base_url = "http://www.google.com/search?q="

# query = input("Please enter your search query: ")

# webbrowser.get(chrome_path).open_new(base_url+query)



# """url = 'www.stackoverflow.com'
#             chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
#             webbrowser.get(chrome_path).open(url)
# """
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(fontstyle.apply('Listening...', 'blue/bold'))
        audio = r.listen(source)
        
    try:
        print(fontstyle.apply('Recognizing...', 'blue/bold'))
        query = r.recognize_google(audio, language = 'en-in')
        print(fontstyle.apply(f'User said: {query}\n', 'blue/bold'))
    except (sr.UnknownValueError, sr.RequestError):
        print(fontstyle.apply('Can\'t recognize! Say that again please', 'blue/bold'))
    return query 


while True:
    
    
    query = takeCommand()

    
    if 'search' and 'google' in query.lower():
                chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

                base_url = "http://www.google.com/search?q="
                
                print(fontstyle.apply('What should I search?', 'blue/bold'))
                speak('What should I search?')

                query = takeCommand()

                webbrowser.get(chrome_path).open_new(base_url+query)