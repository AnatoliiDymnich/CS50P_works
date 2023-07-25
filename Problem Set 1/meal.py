def main():
    t = input("What time is it? ")
    t = convert(t)
    if 7.0 <= t <= 8.0:
        print("breakfast time")
    elif 12.0 <= t <= 13.0:
        print("lunch time")
    elif 18.0 <= t <= 19.0:
        print("dinner time")

def convert(time):
    hour, minutes = time.split(":")
    minutes = float(minutes) / 60
    return float(hour) + minutes

if __name__ == "__main__":
    main()
