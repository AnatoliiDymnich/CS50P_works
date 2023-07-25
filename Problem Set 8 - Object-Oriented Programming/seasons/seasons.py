"""program prompts the user for their date of birth in YYYY-MM-DD format and then sings prints
how old they are in minutes, rounded to the nearest integer, using English words instead of numerals,
just like the song from Rent, without any and between words. Since a user might not know the time at
which they were born, assume, for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date.
And assume that the current time is also midnight. In other words, even if the user runs the program at noon,
assume that it's actually midnight, on the same date."""

import sys, inflect
from datetime import date


def main():
    date = check_date(get_date())
    minutes = convert_to_minutes(find_delta_days(date))
    print(f'{convert_minutes_to_words(minutes)} minutes')


def get_date():
    return input("Date of Birth: ").strip()


def check_date(date):
    try:
        y, m, d = date.split("-")
    except ValueError:
        sys.exit("Invalid date")

    if not y.isdigit() or not m.isdigit() or not d.isdigit():
        sys.exit("Invalid date")

    if len(y) != 4 or len(m) != 2 or len(d) != 2:
        sys.exit("Invalid date")

    if int(m) > 12 or int(d) > 31:
        sys.exit("Invalid date")

    return [int(y), int(m), int(d)]


def find_delta_days(d):
    delta = date.__sub__(date.today(), date(d[0], d[1], d[2]))
    string_delta = f'{delta}'
    list_delta = string_delta.split(" ")
    return list_delta[0]


def convert_to_minutes(days):
    return int(days) * 24 * 60


def convert_minutes_to_words(min):
    minutes_str = inflect.engine().number_to_words(min)
    minutes_str = minutes_str.capitalize().replace(" and ", " ")
    return minutes_str


if __name__ == "__main__":
    main()
