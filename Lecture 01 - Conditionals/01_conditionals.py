#############################################################
#                       Conditionals                        #
#############################################################
# Conditionals empower your program to make decisions—like choosing between two paths at a fork in the road—based on specific conditions. They enable your code to respond dynamically, executing different actions depending on the situation.

# Basic comparison with if / elif / else
def main1():
    x = int(input("What's x? "))
    y = int(input("What's y? "))

    if x < y:
        print("x is less than y")
    elif x == y:
        print("x and y are equal")
    else:
        print("x is greater than y")


# Alternative way using logical operators
def main2():
    x = int(input("What's x? "))
    y = int(input("What's y? "))

    if x < y or x > y:  # equivalent to: if x != y
        print("x is not equal to y")
    else:
        print("x and y are equal")


# Using conditional logic for letter grading
def grade():
    score = int(input("Score: "))

    if score >= 90 and score <= 100:  # using AND explicitly
        print("Grade: A")
    elif 80 <= score < 90:  # Pythonic range check
        print("Grade: B")
    elif score >= 70:  # Already checked for 90 and 80 above
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")


# Checking even or odd
def parody():
    x = int(input("What's x? "))

    if x % 2 == 0:
        print("x is even")
    else:
        print("x is odd")


#############################################################
#                         Booleans                          #
#############################################################

# Classic boolean function
def is_even(x):
    if x % 2 == 0:
        return True  # Note: Capital T for True
    else:
        return False  # Capital F for False


# Ternary operator: readable and Pythonic
def is_even_pythonic(x):
    return True if x % 2 == 0 else False


# Cleanest and most Pythonic
def is_even_best(y):
    return y % 2 == 0  # returns a boolean directly


# Using the helper function in logic
def check_even():
    x = int(input("What's x? "))

    if is_even_best(x):
        print("x is even")
    else:
        print("x is odd")


#############################################################
#                           Match                           #
#############################################################

# Pattern matching (Python 3.10+)
def house():
    name = input("What's your name? ").capitalize()

    match name:
        case "Harry" | "Hermione" | "Ron":
            print("Griffindor")
        case "Draco":
            print("Slytherin")
        case _:  # default / fallback case
            print("Who?")


# Run the match example
house()
