"""program in Python that prompts the user for mass as an integer (in kilograms)
and then outputs the equivalent number of Joules as an integer.
Assume that the user will input an integer."""

mass = input("m: ")
c = 300000000

E = int(mass) * c**2

print("E: ", E)
