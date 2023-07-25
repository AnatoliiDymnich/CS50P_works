"""program prompts the user for a vanity plate and then output Valid if meets all of the requirements
or Invalid if it does not. Assume that any letters in the user's input will be uppercase.
is_valid returns True if 's' meets all requirements and False if it does not. Assume that 's' will be a str.
Requirements:
- “All vanity plates must start with at least two letters.”
- “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
- “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
- “No periods, spaces, or punctuation marks are allowed.” """

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    forbidden_symbols = [" ", ".", ","]
    check_num = []
    if 2 <= len(s) <= 6:
        for i in s:
            if i in forbidden_symbols:
                return False
        for i in s:
            if i in numbers:
                check_num.append(i)
        if len(check_num) > 0:
            for i in range(1, len(check_num)+1):
                if s[-i] not in numbers:
                    return False
            if check_num[0] == "0":
                return False
        if s[0] in numbers or s[1] in numbers:
            return False
        else:
            return True

main()
