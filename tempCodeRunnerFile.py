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
                ('Enter 1 for easy mode, 2 for medium mode, 3 for hard mode 4 for the impossible mode and 5 for OVERLOAD difficulty!!!'))
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