from main import *
import webbrowser

chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

base_url = "http://www.google.com/search?q="

print(fnt.apply('What should I search?', 'blue/bold'))
speak('What should I search?')

query = takeCommand()
webbrowser.get(chrome_path).open_new(base_url+query)
