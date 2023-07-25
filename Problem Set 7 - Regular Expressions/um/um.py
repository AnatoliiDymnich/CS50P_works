"""program called count that expects a line of text as input as a str and returns, as an int,
the number of times that “um” appears in that text, case-insensitively, as a word unto itself,
not as a substring of some other word. For instance, given text like hello, um, world, the function should return 1.
Given text like yummy, though, the function should return 0."""

import re


def main():
    print(count(input("Text: ")))


def count(s):
    count = re.findall(r"(\b|\s)um(\b|\s)", s, re.IGNORECASE)
    return len(count)



if __name__ == "__main__":
    main()
