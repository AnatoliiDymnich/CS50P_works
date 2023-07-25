"""program expects exactly one command-line argument, the name (or path) of a CSV file
in Pinocchio's format, and outputs a table formatted as ASCII art using tabulate.
Format the table using the library's grid format. If the user does not specify exactly
one command-line argument, or if the specified file's name does not end in .csv,
or if the specified file does not exist, the program should instead exit via sys.exit."""

import sys, csv, tabulate


try:
    if len(sys.argv) < 2:
        sys.exit("Too few line-arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many line-arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
except IndexError:
    pass


pizzas = []

with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
             pizzas.append(row)


print(tabulate.tabulate(pizzas, headers="keys", tablefmt="grid"))
