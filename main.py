import pyfiglet, sys, random

def textToAscii(text, font):
    asciiArt = pyfiglet.figlet_format(text, font = font)
    return asciiArt

def boldText(text):
    return "\033[1m" + text + "\033[0m"

def main():
    print("Welcome to the B33FWare ASCII Text2Art Converter.")
    print("Author: Steven Blake Tobias")
    print("More info at" + boldText(" www.github.com/s-b-t"))
    print()
    input('Press ' + boldText("[Enter]") + ' or ' + boldText("[Return]") + ' to continue...')
    print()

    fonts = pyfiglet.FigletFont.getFonts()
    currentFont = None
    
    while True:
        userText = input('Enter or paste the text you would like to convert to ASCII art' + boldText(" (to Quit, type QUIT): "))
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
                useSameFont = input("Do you want to continue with the same font?" + boldText(" (Y/N): "))
                print()
                if useSameFont.lower().upper() in ['y', 'n', 'yes', 'no', 'Y', 'N', 'Yes', 'No', 'YES', 'NO' ]:
                    break
                else: 
                    print("You didn't choose an answer!" + boldText(' (Y/N): '))
                    print()
            if useSameFont.lower().upper() in ['y', 'yes', 'Y', 'Yes', 'YES']:
                fontToUse = currentFont
            else: 
                fontToUse = random.choice(fonts)
        else:
            fontToUse = random.choice(fonts)

        asciiArt = textToAscii(userText, fontToUse)
        print(asciiArt)
        print(boldText("Current Font: ") + f'{fontToUse}')
        print()

        currentFont = fontToUse

        if (asciiArt):
            continue
        break
        
if __name__ == "__main__":
    main()