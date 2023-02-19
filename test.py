import pyttsx3

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
shoutoutlist = ["Prithvi", "Harry", "Ashneer Grover"]
for name in shoutoutlist:
    speak(f"Shout Out to {name}")