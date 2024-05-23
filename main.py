import pyfiglet, sys, random

# Defines textToAscii function by formatting incoming data to match text and font/allows asciiArt to be used
def textToAscii(text, font):
    asciiArt = pyfiglet.figlet_format(text, font = font)
    return asciiArt

# Boldens text using ANSI escape characters when function is called
def boldText(text):
    return "\033[1m" + text + "\033[0m"

# Italicizes text using ANSI escape characters when function is called
def italicText(text):
    return "\033[3m" + text + "\033[0m"

def main():
    # preferredFonts = [] 
    # Pseudo code: This will give the user a random font from a predetermined font list only out of the legible fonts that I select for the program to run off of
    
    # Greets user with header
    print()
    print("Welcome to the B33FWare ASCII Text2Art Converter.")
    print("Author: Steven Blake Tobias")
    print("More info at" + boldText(" www.github.com/s-b-t"))
    print()
    
    # Allows user to continue with the program as intended
    input('Press ' + boldText("[Enter]") + ' or ' + boldText("[Return]") + ' to continue...')
    print()

    # Grabs fonts from pyfiglet, initially sets currentFont to default of None
    fonts = pyfiglet.FigletFont.getFonts()
    currentFont = None
    
    # Validates and keeps asking user to enter something if no valid entry exists
    while True:
        
        # Allows user to enter any text they wish, or QUIT out of the program
        userText = input('Enter or paste the text you would like to convert to ASCII art' + boldText(" (to Quit, type QUIT): "))
        print()

        # If there's no input from the user, program alerts user
        if not (userText):
            print('You didn\'t provide any text!')
            print()
            continue
        
        # If user wishes to leave the program, prints a Thank You message and exits the program
        if userText == 'QUIT':
            print('Thank you for using the B33FWare ASCII Text2Art Converter.')
            sys.exit()
        
        # As long as the currentFont is active, sets a condition to give the user more options on changing the font style or keeping the same font style
        if currentFont:
            
            # Keeps asking user to enter valid input of Y/N
            while True:
                
                # Gives user the option to continue with the same font or not
                useSameFont = input("Do you want to continue with the same font?" + boldText(" (Y/N): "))
                print()
                
                # If answer is Yes or No (in any type-case), continues the program as intended
                if useSameFont.lower() in ['y', 'n', 'yes', 'no', 'Y', 'N', 'Yes', 'No', 'YES', 'NO' ]:
                    break
                else:
                    
                    # Validates to user that they didn't choose an answer if no input was entered
                    print("You didn't choose an answer!" + boldText(' (Y/N): '))
                    print()
            
            if useSameFont.lower() in ['y', 'yes', 'Y', 'Yes', 'YES']:
                fontToUse = currentFont
            
            # If user says Yes (in any type-case), program keeps the same font, otherwise chooses a font at random from pyfiglet
            
            else: 
                fontToUse = random.choice(fonts)
        else:
            fontToUse = random.choice(fonts)

        # Prints the ASCII art to terminal and names the Current Font
        asciiArt = textToAscii(userText, fontToUse)
        print(asciiArt)
        print(boldText("Current Font: ") + italicText(f'{fontToUse}'))
        print()

        currentFont = fontToUse

        # If ASCII art is indeed printed to terminal, program keeps going.. Otherwise breaks the main loop
        if (asciiArt):
            continue
        break
        
if __name__ == "__main__":
    main()