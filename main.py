import pyfiglet, sys

def textToAscii(text):
    asciiArt = pyfiglet.figlet_format(text)
    return asciiArt

def main():
    
    while True:
        userText = input('Enter or paste the text you would like to convert to ASCII art (to stop, type QUIT): ')
        print('\n')

        if userText == 'QUIT':
            print('Thanks for using the B33FWARE ASCII art generator!')
            sys.exit()

        if not (userText):
            print('You didn\'t enter anything!')
            print('\n')
            continue
        
        asciiArt = textToAscii(userText)
        print(asciiArt)

        if (asciiArt):
            continue
        break
        
if __name__ == "__main__":
    main()