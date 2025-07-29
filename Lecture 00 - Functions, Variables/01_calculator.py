##############################################################
#                         Integers                           #
##############################################################

x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)  # Convert both strings to integers, then add
print(z)

# Nesting functions — an exaggerated compact version
print("")
print(int(input("What's x? ")) + int(input("What's y? ")))  # Inputs and adds in one line


##############################################################
#                          Floats                            #
##############################################################

x = float(input("What's x? "))  # Convert user input to float
y = float(input("What's y? "))

print(x + y)  # Adds two floats

# Rounding the result using round(number, ndigits)
print(round(x + y, 0))  # Rounds to nearest integer (still returns float if 2nd argument is given)

z = round(x + y)
print(f"{z}")       # Print rounded result as integer
print(f"{z:,}")     # Adds thousands separator (e.g., 1,000)


"""
Divisions
---------
Examples of dividing floats and formatting results:
- round(x / y, 2): rounds the result to 2 decimal places
- f"{value:.2f}": formats a float to two decimal digits using f-string
"""

z = round(x / y, 2)               # Rounded result stored in z
print(f"{(x / y):.2f}")           # Same result, formatted directly in the print
