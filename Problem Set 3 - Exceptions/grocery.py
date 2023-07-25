"""program prompts the user for items, one per line, until the user inputs control-d
(which is a common way of ending one's input to a program).
Then output the user's grocery list in all uppercase, sorted alphabetically by item,
prefixing each line with the number of times the user inputted that item. No need to pluralize the items.
Treat the user's input case-insensitively."""

p_list = {}

while True:
    try:
        item = input().lower().strip()
        if item not in p_list:
            p_list[item] = 1
        else:
            p_list[item] += 1
    except EOFError:
        products = list(p_list.keys())
        products.sort()
        for i in products:
            print(f"{p_list[i]} {i.upper()}")
        break
