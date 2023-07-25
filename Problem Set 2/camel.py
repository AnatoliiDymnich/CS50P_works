"""program prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case.
Assume that the user's input will indeed be in camel case."""

name = input("camelCase: ")
snake_name = ""

for i in name:
    if i.isupper():
        snake_name += i.replace(i, '_' + i.lower())
    else:
        snake_name += i

print("snake_case:", snake_name)
