"""program prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636
Then output that same date in YYYY-MM-DD format. If the user's input is not a valid date in either format, prompt the user again.
Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days."""

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date_to_convert = input("Date: ")
        if "/" in date_to_convert:
            m, d, y = date_to_convert.split("/")
            m, d, y = int(m), int(d), int(y)
            if d > 31 or m > 12:
                continue
            else:
                print(f"{y}-{m:02}-{d:02}")
                break
        else:
            date_to_convert = date_to_convert.split(" ")
            m, d, y = date_to_convert
            if "," in d:
                d = d.replace(",", "")
                if m in months:
                    m = months.index(m) + 1
                    m, d, y = int(m), int(d), int(y)
                    if d > 31 or m > 12:
                        continue
                    else:
                        print(f"{y}-{m:02}-{d:02}")
                        break
                else:
                    continue
    except ValueError:
        pass
