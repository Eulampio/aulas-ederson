# import pyfiglet
# text= "Ola, mundo"
# ascii_art= pyfiglet.figlet_format(text)
# print(ascii_art)

# import pyfiglet
# text= "vida depois de amanha"
# ascii_art_standarte= pyfiglet.figlet_format(text, font="standard")
# print(ascii_art_standarte)
# ascii_art_standarte= pyfiglet.figlet_format(text, font="slant")
# print(ascii_art_standarte)

from colorama import Fore,Style
import pyfiglet
from colorama import init
text= "vida que segue"
ascii_art= pyfiglet.figlet_format(text, font="slant")
ascii_art= pyfiglet.figlet_format(text, font="slant")
print(Fore.CYAN+ Style.BRIGHT+ ascii_art)
print(Fore.RED+ Style.BRIGHT+ ascii_art)
print(Fore.BLUE+ Style.BRIGHT+ ascii_art)
print(Fore.RED+ Style.BRIGHT+ ascii_art)

