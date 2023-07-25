"""program expects exactly one command-line argument, the name (or path) of a Python file,
and outputs the number of lines of code in that file, excluding comments and blank lines.
If the user does not specify exactly one command-line argument, or if the specified file's name
does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.
Assume that any line that starts with #, optionally preceded by whitespace, is a comment.
(A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank."""

import sys


try:
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif sys.argv[1].endswith(".py") != True:
        sys.exit("Not a Python file")
    file = open(sys.argv[1])

except IndexError:
    pass
except FileNotFoundError:
    sys.exit("File does not exist")

count_row = 0
for row in file.readlines():
    if row.isspace() or row.lstrip().startswith("#"):
        continue
    else:
        count_row += 1

print(count_row)
