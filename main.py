import pyfiglet, sys

def textToAscii(text):
    asciiArt = pyfiglet.figlet_format(text)
    return asciiArt

def main():
    
    print('Welcome to the B33FWare ASCII Text2Art Converter.')
    print('Author: Steven Blake Tobias')
    print('\n')
    input('Press [Enter] or [Return] to continue...')
    print('\n')

    while True:
        userText = input('Enter or paste the text you would like to convert to ASCII art (to Quit, type QUIT): ')
        print('\n')

        if userText == 'QUIT':
            print('Thanks for using the B33FWare ASCII Text2Art Converter!')
            sys.exit()

        if not (userText):
            print('You didn\'t enter anything!')
            print('\n')
            continue
        
        asciiArt = textToAscii(userText)
        print(asciiArt)
        print('\n')

        if (asciiArt):
            continue
        break
        
if __name__ == "__main__":
    main()