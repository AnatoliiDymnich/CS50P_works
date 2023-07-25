"""program accepts a str as input and returns that same input
with any :) converted to 🙂 (otherwise known as a slightly smiling face)
and any :( converted to 🙁 (otherwise known as a slightly frowning face).
All other text should be returned unchanged."""

def main():
    phrase = input()
    new_phrase = convert(phrase)
    print(new_phrase)

def convert(t):
    t = t.replace(":)", "🙂").replace(":(", "🙁")
    return t

main()
