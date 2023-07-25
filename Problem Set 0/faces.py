def main():
    phrase = input()
    new_phrase = convert(phrase)
    print(new_phrase)

def convert(t):
    t = t.replace(":)", "🙂").replace(":(", "🙁")
    return t

main()
