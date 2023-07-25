"""program prompts the user for a str in English and then outputs the “emojized” version of that str,
converting any codes (or aliases) therein to their corresponding emoji."""

import emoji

text = input("Input: ").strip()
print(emoji.emojize(f'Output: {text}', language="alias"))
