### B33FWare ASCII Text2Art Converter
![B33FWare2](https://github.com/s-b-t/ascii-art-converter/assets/109566542/6106cd7d-55b2-4960-964b-d7ee80ece667)


*This program is still in its BETA/WIP stage. I will be updating more functionality and features continually.*

```pyfiglet``` is used to pull in the different styles of fonts.

If you want to check out more information about ```pyfiglet```, visit https://pypi.org/project/pyfiglet/.

This program is meant showcase how creative you can be right in your terminal. It converts any text you want into ASCII art.

I hand-picked the coolest and most legible fonts from ```pyfiglet``` as there are more than a few fonts in the library that may not be desirable to the eye. The program uses ```handPickedFontsOmitLast = [font for font in handPickedFonts if font != lastFontUsed]``` and ```fontToUse = random.choice(handPickedFontsOmitLast)``` to determine a random font out of the hand-picked list, but also ensures that it does not pick the last font that was previously used.

To get started, navigate to ```ascii-art-converter``` in your terminal (assuming you've already imported the code and named your folder ```ascii-art-converter```).

Type the following command to install pyfiglet to ```ascii-art-converter```: ```pip install pyfiglet```

Once you've verified ```pyfiglet``` was fully installed, type and enter the following command:
  
  Windows: ```python main.py```
  
  MacOS: ```python3 main.py```

Once you've received the greeting message/header, enter whatever text you want and watch the magic happen!
