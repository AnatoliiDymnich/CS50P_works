"""program expects a str of HTML as input, extracts any YouTube URL that's the value
of a src attributeof an iframe element therein, and returns its shorter, shareable youtu.be
equivalent as a str. Assume that the value of src will be surrounded by double quotes.
And assume that the input will contain no more than one such URL. If the input does not contain
any such URL at all, return None. Expect that any such URL will be in one of the formats below:
- <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
- src="https://www.youtube.com/embed/xvFZjo5PgG0" """

import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if check := re.search(r"youtube\.com/embed/(\w+)\"", s):
        link = check.group(1)
    else:
        return None

    return f"https://youtu.be/{link}"



if __name__ == "__main__":
    main()
