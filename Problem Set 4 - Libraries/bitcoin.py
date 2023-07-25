"""program requirements:
- Expects the user to specify as a command-line argument the number of Bitcoins, 'n',
that they would like to buy. If that argument cannot be converted to a float,
the program should exit via sys.exit with an error message.
- Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json,
which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float
- Outputs the current cost of 'n' Bitcoins in USD to four decimal places, using ',' as a thousands separator."""


import requests, sys


# make request and catch course
req = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

r = req.json()
course = r["bpi"]["USD"]["rate_float"]

# input count from user, if not float - exit
try:
    count_usd = float(sys.argv[1])
except IndexError:
    sys.exit("Missing comand-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

# outputs current cost in USD to four decimal places,
# using coma as the thousands separator
curr_cost = float(course) * count_usd

print(f'${curr_cost:,}')
