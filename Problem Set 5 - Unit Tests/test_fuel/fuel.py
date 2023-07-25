def main():
    frac = input("Fraction: ")
    print(gauge(convert(frac)))


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x, y = int(x), int(y)
        if y == 0:
            raise ZeroDivisionError
        elif x > y:
            raise ValueError
        result = x / y * 100
    except(ValueError):
        raise
    else:
        return result


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
