### Welcome to the B33FWare ASCII Text2Art Converter!

*Please Note: This program is in its BETA/WIP stage*

```pyfiglet``` is used to pull in the different styles of fonts

If you want to check out more information about ```pyfiglet```, visit https://pypi.org/project/pyfiglet/

This program is meant showcase how creative you can be right in your terminal. It converts any text you want into ASCII art. Terminal programs are fun!

I hand-picked the coolest and most legible fonts from ```pyfiglet``` as there are more than a few fonts in the library that may not be desirable to the eye. The program uses ```predeterminedFontsExcludingLast = [font for font in predeterminedFonts if font != lastFontUsed]``` and ```fontToUse = random.choice(predeterminedFontsExcludingLast)``` to determine a random font out of the hand-picked list.

To get started, navigate to ```ascii-art-converter``` in your terminal (assuming you've already imported the code and named your folder ```ascii-art-converter```).

Once you're there, type and enter the following command:
  
  Windows: ```python main.py```
  
  MacOS: ```python3 main.py```

Once you've received the greeting message/header, enter whatever text you want and watch the magic happen!
