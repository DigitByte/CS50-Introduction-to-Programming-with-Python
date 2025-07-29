#############################################################
#                         Functions                         #
#############################################################
# Functions are verbs or actions that the computer or computer language will already know how to perform.

def main():
    name = input("What is your name? ")
    hello()          # Uses the default value of the `to` parameter
    hello(name)      # Passes user input to the `hello()` function

    x = int(input("What's x? "))
    print(f"{x} squared is {square(x)}")  # Call square function and print result


# Function to return the square of a number
def square(n):
    return n**2  # Equivalent to: n * n or pow(n, 2)


# Function with a default parameter
def hello(to="World"):
    print(f"Hello, {to}!")


# Call main() to run the program
# Note: In Python, functions can be defined after main() as long as they are called later
main()
