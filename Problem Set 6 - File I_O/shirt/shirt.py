"""program expects exactly two command-line arguments:
- in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
- in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
The program should then overlay shirt.png (which has a transparent background) on the input
after resizing and cropping the input to be the same size, saving the result as its output."""

import sys, os
from PIL import Image, ImageOps


def main():
    check_input_params()
    put_on_shirt()

def put_on_shirt():
    shirt = Image.open("shirt.png")
    before = Image.open(sys.argv[1])
    shirt_size = shirt.size
    resized = ImageOps.fit(before, shirt_size)
    resized.paste(shirt, shirt)
    resized.save(sys.argv[2])

def check_input_params():
    formats = [".jpg", ".jpeg", ".png"]
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif os.path.splitext(sys.argv[1])[1].lower() not in formats or os.path.splitext(sys.argv[2])[1].lower() not in formats:
        sys.exit("Invalid input")
    elif os.path.splitext(sys.argv[1])[1].lower() != os.path.splitext(sys.argv[2])[1].lower():
        sys.exit("Input and output have different extensions")
    try:
        open(sys.argv[1]).closed
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()