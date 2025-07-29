#############################################################
#                         Exceptions                        #
#############################################################

# Exceptions are unexpected issues that occur while your program is running.
#They disrupt the normal flow of execution and typically indicate that something
# has gone wrong, such as invalid input, missing files, or logical errors.

def number():
    try:
        x = int(input("Enter a number: "))
    except ValueError:
        print("Please, enter an integer")
    else:
        print(f"x is {x}")


def get_number():
    while True:
        try:
            x = int(input("Enter a number: "))
        except ValueError:
            print("Please, enter an integer")
        else:
            return x


def get_number_shorter():
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            print("Please, enter an integer")


def get_number_pass():
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            pass


def get_int(prompt="Please, enter an integer: "):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


main()
