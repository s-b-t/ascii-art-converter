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
    print('\n')
    
    while True:
        userText = input('Enter or paste the text you would like to convert to ASCII art (to Quit, type QUIT): ')
        print('\n')

        if not (userText):
            print('You didn\'t enter anything!')
            print('\n')
            continue

        if userText == 'QUIT':
            print('Thanks for using the B33FWare ASCII Text2Art Converter!')
            sys.exit()
        
        if currentFont:
            useSameFont = input('Do you want to continue with the same font? (Y/N): ')
            print('\n')
            # Line 30-34 bugged. Must resolve program only being able to accept Y/N answers for both inputs (31 and 35). Program allows user to just hit Enter or type in a word that generates ASCII (NOT VALID INPUT FOR THESE INPUTS!). Program needs to function just like lines 18-24. Input on Line 35 randomizes no matter yes/no. Yes/no input on line 31 work just fine.
            if not (useSameFont):
                input('Please answer (Y/N): ')
                print('\n')
            # Line 35-42 there's another bug. When user inputs 'y' the output does not keep the font the same and randomizes instead. Potential problem/placement with while loop. Also need more validations just like note on Line 34.
            if useSameFont.lower() == 'y':
                fontToUse = currentFont
            else: 
                fontToUse = random.choice(fonts)
        else:
            fontToUse = random.choice(fonts)

        asciiArt = textToAscii(userText, fontToUse)
        print(asciiArt)
        print('\n')

        currentFont = fontToUse

        if (asciiArt):
            continue
        break
        
if __name__ == "__main__":
    main()