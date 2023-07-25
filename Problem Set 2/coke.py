"""program prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
Assume that the user will only input integers, and ignore any integer that isn't an accepted denomination."""

cost = 50

while cost > 0:
    print("Amount Due:", cost)
    left_to_enter = int(input("Insert coin: "))
    if left_to_enter == 25 or left_to_enter == 10 or left_to_enter == 5:
        cost = cost - left_to_enter


print("Change Owed:", abs(cost))
