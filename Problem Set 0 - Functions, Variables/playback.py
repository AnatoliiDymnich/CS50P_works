"""program prompts the user for input and then outputs that same input,
replacing each space with ... (i.e., three periods)."""

phrase = input()

phrase = phrase.replace(" ", "...")

print(phrase)
