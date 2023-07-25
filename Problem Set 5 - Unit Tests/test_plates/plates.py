def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    forbidden_symbols = [" ", ".", ",", "!", "?"]
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
        if s[0].isalpha() == False or s[1].isalpha() == False:
            return False
        else:
            return True
    else:
        return False

if __name__ == "__main__":
    main()
