import sys


def name():
    # Check number of arguments (expecting exactly 1)
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments")

    # sys.argv[1] is the first argument after the script name
    print("Hello, my name is", sys.argv[1].capitalize())


def names():
    # Check for at least one name argument
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")

    # Loop through all arguments after script name
    for name in sys.argv[1:]:
        print("Hello, my name is", name.capitalize())


def main():
    # Call either function
    # name()
    names()


# Ensures `main()` runs only if this file is executed directly
if __name__ == "__main__":
    main()
    