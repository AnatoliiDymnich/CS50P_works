"""program that prompts the user for a str of text
and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase."""

text = input("Input: ")
vowels = ["a", "e", "i", "o", "u"]
new_text = ""

for i in text:
    if i.lower() not in vowels:
        new_text += i

print(new_text)
