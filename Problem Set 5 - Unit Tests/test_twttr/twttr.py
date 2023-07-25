def main():
    text = input("Input: ")
    print(shorten(text))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    text = ""
    for i in word:
        if i.lower() not in vowels:
            text += i
    return text

if __name__ == "__main__":
    main()
