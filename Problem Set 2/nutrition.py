"""program prompts users to input a fruit (case-insensitively)
and then outputs the number of calories in one portion of that fruit, per the FDA's poster for fruits,
which is also available as text. Capitalization aside,
assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry).
Ignore any input that isn't a fruit."""

fruit = input("Item: ").lower().strip()

calories = {
    "apple": 130,
    "banana": 110,
    "avocado": 50,
    "sweet cherries": 100,
    "kiwifruit": 90,
    "pear": 100
    }

if fruit in calories:
    print(f"Calories: {calories[fruit]}")
