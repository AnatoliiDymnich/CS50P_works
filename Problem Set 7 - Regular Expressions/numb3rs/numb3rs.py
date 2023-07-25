"""program expects an IPv4 address as input as a str and then returns True or False,
respectively, if that input is a valid IPv4 address or not."""

import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if check := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        if 1 <= int(check.group(1)) <= 255 and 0 <= int(check.group(2)) <= 255 and 0 <= int(check.group(3)) <= 255 and 0 <= int(check.group(4)) <= 255:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
