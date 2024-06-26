import pyfiglet, sys, random, os, time

# Defines how animateAscii writes the infoText characters 1 by 1 in .025s intervals giving the impression the program is typing to the user
def animateAscii(infoText, iterations):
    for _ in range(iterations):
        for char in infoText:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.025)

# Function to display the content of the infoText as well as animate the infoText in 1 iteration when user runs the program
def displayWelcomeMessage():
    infoText = "\nWelcome to the " + boldText('B33FWare ASCII Text2Art Converter') + "." + "\nAuthor: Steven Blake Tobias\n" + boldText("PSSST! ") + "This program runs best on full screen.\n" + "More info at " + boldText('www.github.com/s-b-t\n\n')
    iterations = 1
    animateAscii(infoText, iterations)

def displayByeMessage():
    byeText = "Thank you for using the " + boldText('B33FWare ASCII Text2Art Converter') + "." + " Goodbye!"
    iterations = 1
    animateAscii(byeText, iterations)

# Defines the transfer from text into a chosen ASCII font into ASCII Art from pyfiglet
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
    # Defines the predetermined list of fonts
    handPickedFonts = ["block", "banner", "starwars", "slant", "doh", "bubble", "4max", "nancyj-improved", "c_ascii_", "ansi_regular", "cola", "f15_____", "georgia11", "amc_neko", "italics_", "relief", "nscript", "small_shadow", "flipped", "line_blocks", "cli8x8", "relief2", "js_bracket_letters", "colossal", "script", "gothic__", "ansi_shadow", "double", "clr8x10", "xbritebi", "univers", "isometric1", "red_phoenix", "amc_untitled", "cybermedium", "chunky", "broadway", "xsansb", "demo_m__", "js_cursive", "wavy", "ascii_new_roman", "italic", "small_slant", "fourtops", "pepper", "script__", "old_banner", "sub-zero", "xttyb", "binary", "crazy", "rectangles", "linux", "xbrite", "ttyb", "shadow", "bell", "calgphy2", "charact6", "smshadow", "banner3-d", "britei", "big_money-nw", "caligraphy", "glenyn", "thorned", "npn_____", "speed", "drpepper", "xsbookb", "threepoint", "doom", "fire_font-s", "patorjk's_cheese", "char2___", "banner4", "utopiabi", "heart_left", "pyramid", "mini", "dotmatrix", "3-d", "standard", "patorjk-hex", "sblood", "rammstein", "braced", "os2", "t__of_ap", "marquee", "fire_font-k", "filter", "modular", "jazmine", "peaks"]
    
    # Allows user to continue with the program as intended
    input('Press ' + boldText("[Enter]") + ' or ' + boldText("[Return]") + ' to continue...\n')
    
    currentFont = None
    lastFontUsed = None
    
    while True:
        # Allows user to enter any text they wish, or QUIT out of the program
        userText = input('Enter or paste the text you would like to convert to ASCII art ' + boldText('(to Quit, type QUIT)') + ": ")
        print()

        # If user does not enter any text into the prompt, alert the user and keep displaying alert message until they enter valid input
        if not userText:
            print('You didn\'t provide any text!')
            print()
            continue
        
        # Allows user to quit out of the program. If user quits, animated Bye message displays and exits the program
        if userText == 'QUIT':
            displayByeMessage()
            print('\n')
            sys.exit()
        
        # If currentFont is active and while that is true, the program gives user the option to use the same font or not
        if currentFont:
            while True:
                # Gives user the option to continue with the same font or not
                useSameFont = input("Do you want to continue with the same font?" + boldText(" (Y/N)") + ": ")
                print()
                
                # If answer is Yes or No (in any type-case), continues the program as intended
                if useSameFont.lower() in ['y', 'n', 'yes', 'no', 'Y', 'N', 'Yes', 'No', 'YES', 'NO' ]:
                    break
                else:
                    # Validates to user that they didn't choose an answer if no input was entered
                    print("You didn't choose an answer!" + boldText(' (Y/N)') + ":")
                    print()
            
            # Accepts any type-case 'Yes' answer to be recorded and keeps the same font, otherwise randomly selects font if Yes is not the answer
            if useSameFont.lower() in ['y', 'yes', 'Y', 'Yes', 'YES']:
                fontToUse = currentFont
            else:
                # Randomly selects a font from handPickedFonts excluding the last font used if user answer is 'No' or anything but 'Yes'
                handPickedFontsOmitLast = [font for font in handPickedFonts if font != lastFontUsed]
                fontToUse = random.choice(handPickedFontsOmitLast)
        else:
            fontToUse = random.choice(handPickedFonts)

        # Takes the text entered by the user along with the chosen font, and stores it to generate the corresponding art into asciiArt
        asciiArt = textToAscii(userText, fontToUse)

        # Gets terminal width
        terminalWidth = os.get_terminal_size().columns

        # Takes the ASCII art, centers each line within the terminal width, and prints the resulting centered ASCII art to the terminal
        # print("\n\n")
        # print(handPickedFonts)
        print("\n\n")
        print("\n".join([line.center(terminalWidth) for line in asciiArt.splitlines()]))
        print("\n\n")

        # Centers 'Current Font: fontToUse' statement to terminal underneath the centered ASCII art
        currentFontText = boldText("Current Font: ") + italicText(f'{fontToUse}')
        padding = (terminalWidth - len(currentFontText)) // 2
        print(" " * padding + currentFontText)
        print("\n\n")

        currentFont = fontToUse
        lastFontUsed = fontToUse

if __name__ == "__main__":
    displayWelcomeMessage()
    main()