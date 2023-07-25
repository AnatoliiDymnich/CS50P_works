"""program prompts the user for the answer to the Great Question of Life, the Universe and Everything,
outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two.
Otherwise output No."""

answer = input("What is the Answer? ").strip().lower()

match answer:
    case "forty two" | "forty-two" | "42":
        print("Yes")
    case _:
        print("No")
