"""program expects a str in either of the 12-hour formats below and returns the corresponding str
in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein)
and that there will be a space before each. Assume that these times are representative of actual times,
not necessarily 9:00 AM and 5:00 PM (or 9 AM to 5 PM) specifically. Raise a ValueError instead if the input to convert
is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.)."""

import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if hour := re.search(r"^([01]?\d)(?::(\d\d))? (AM|PM) to ([01]?\d)(?::(\d\d))? (AM|PM)$", s):
        from_hour = hour.group(1)
        to_hour = hour.group(4)
        if not 0 < int(from_hour) < 13 or not 0 < int(to_hour) < 13:
            raise ValueError
    else:
        raise ValueError

    if hour.group(2) == None:
        from_minutes = 0
    else:
        from_minutes = hour.group(2)

    if hour.group(5) == None:
        to_minutes = 0
    else:
        to_minutes = hour.group(5)

    if not 0 <= int(from_minutes) < 60 or not 0 <= int(to_minutes) < 60:
        raise ValueError

    if hour.group(3) == "PM":
        from_hour = int(from_hour) + 12
        if from_hour == 24:
            from_hour = 12
    elif hour.group(3) == "AM":
        if from_hour == "12":
            from_hour = 0

    if hour.group(6) == "PM":
        to_hour = int(to_hour) + 12
        if to_hour == 24:
            to_hour = 12
    elif hour.group(6) == "AM":
        if to_hour == "12":
            to_hour = 0

    return f"{int(from_hour):02}:{int(from_minutes):02} to {int(to_hour):02}:{int(to_minutes):02}"


if __name__ == "__main__":
    main()
