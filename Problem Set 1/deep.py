answer = input("What is the Answer? ").strip().lower()

match answer:
    case "forty two" | "forty-two" | "42":
        print("Yes")
    case _:
        print("No")
