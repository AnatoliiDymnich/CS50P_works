"""implement program:
- Expects zero or two command-line arguments:
- Zero if the user would like to output text in a random font.
- Two if the user would like to output text in a specific font, in which casethe first of
the twoshouldbe -f or --font, and the second of the two should be the name of the font.
- Prompts the user for a str of text.
- Outputs that text in the desired font.
- If the user provides two command-line arguments and the first is not -f or --font or the secon
is not the name of a font, the program should exit via sys.exit with an error message."""

from pyfiglet import Figlet
import sys, random

figlet = Figlet()


if len(sys.argv) == 1:
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)

elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv == "--font":
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

t = input("Input: ")
print(f"Output: {figlet.renderText(t)}")
