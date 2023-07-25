"""program prompts the user for an arithmetic expression and then calculates
and outputs the result as a floating-point value formatted to one decimal place.
Assume that the user's input will be formatted as x y z,
with one space between x and y and one space between y and z"""

expression = input("Expression: ")
x, z, y = expression.split(" ")

if z == "+":
    print(float(x) + float(y))
elif z == "-":
    print(float(x) - float(y))
elif z == "*":
    print(float(x) * float(y))
elif z == "/":
    print(float(x) / float(y))
