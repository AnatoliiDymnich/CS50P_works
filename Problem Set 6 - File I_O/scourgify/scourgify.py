"""program that:
- Expects the user to provide two command-line arguments:
-- the name of an existing CSV file to read as input, whose columns are assumed to be, in order,
-- name and house, and the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
- Converts that input to that output, splitting each name into a first name and last name.
Assume that each student will have both a first name and last name.
- If the user does not provide exactly two command-line arguments, or if the first cannot be read,
the program should exit via sys.exit with an error message."""

import sys, csv


students = []

try:
    if len(sys.argv) < 3:
        sys.exit("Too few line-arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many line-argumetns")
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("not a CSV file")
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].split(",")
            students.append({"first": first.strip(), "last": last, "house": row["house"]})
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")


with open(sys.argv[2], "w", newline="") as file2:
    writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for student in students:
        writer.writerow(student)
