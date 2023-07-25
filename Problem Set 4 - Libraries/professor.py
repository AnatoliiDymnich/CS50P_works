"""game parameters:
- Prompts the user for a level, 'l'. If the user does not input 1, 2, or 3, the program should prompt again.
- Randomly generates ten (10) math problems formatted as 'X + Y = ', wherein each of 'X' and 'Y'
is a non-negativeinteger with  digits. No need to support operations other than addition (+).
- Prompts the user to solve each of those problems. If an answer is not correct (or not even a number),
the program should output 'EEE' and prompt the user again, allowing the user up to three tries in total for that problem.
If the user has still not answered correctly after three tries, the program should output the correct answer.
- The program should ultimately output the user's score: the number of correct answers out of 10."""

import random


def main():
    level = get_level()
    Score = 0
    for i in range(10):
        Score_before = Score
        a, b = generate_integer(level)
        sum = a + b
        for i in range(3):
            try:
                answer = int(input(f'{a} + {b} = '))
            except ValueError:
                print("EEE")
                continue
            if answer == sum:
                Score += 1
                break
            else:
                print("EEE")
                continue
        if Score_before == Score:
            print(f'{a} + {b} = {sum}')
    print(f'Score: {Score}')


def get_level():
    while True:
        try:
            l = int(input("Level: "))
            if 1 <= l <= 3:
                return l
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        a, b = random.randint(0, 9), random.randint(0, 9)
    elif level == 2:
        a, b = random.randint(10, 99), random.randint(10, 99)
    elif level == 3:
        a, b = random.randint(100, 999), random.randint(100, 999)
    return a, b

if __name__ == "__main__":
    main()
