import pyfiglet, sys, random

def textToAscii(text, font):
    asciiArt = pyfiglet.figlet_format(text, font = font)
    return asciiArt

def main():
    fonts = pyfiglet.FigletFont.getFonts()
    currentFont = None
    
    print('Welcome to the B33FWare ASCII Text2Art Converter.')
    print('Author: Steven Blake Tobias')
    print('\n')
    input('Press [Enter] or [Return] to continue...')
    print()
    
    while True:
        userText = input('Enter or paste the text you would like to convert to ASCII art (to Quit, type QUIT): ')
        print()

        if not (userText):
            print('You didn\'t provide any text!')
            print()
            continue

        if userText == 'QUIT':
            print('Thanks for using the B33FWare ASCII Text2Art Converter.')
            sys.exit()
        
        if currentFont:
            while True:
                useSameFont = input('Do you want to continue with the same font? (Y/N): ')
                print()
                if useSameFont.lower().upper() in ['y', 'n', 'yes', 'no', 'Y', 'N', 'Yes', 'No', 'YES', 'NO' ]:
                    break
                else: 
                    print("You didn't choose an answer! (Y/N): ")
                    print()
            if useSameFont.lower().upper() in ['y', 'yes', 'Y', 'Yes', 'YES']:
                fontToUse = currentFont
            else: 
                fontToUse = random.choice(fonts)
        else:
            fontToUse = random.choice(fonts)

        asciiArt = textToAscii(userText, fontToUse)
        print(asciiArt)
        print()

        currentFont = fontToUse

        if (asciiArt):
            continue
        break
        
if __name__ == "__main__":
    main()