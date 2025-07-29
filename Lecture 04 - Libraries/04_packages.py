#############################################################
#                         Packages                          #
#############################################################

# A *package* is a third-party Python library you can install to access
# code written by others — reusable tools, functions, or interfaces.
# Packages are commonly found on **PyPI** (Python Package Index): https://pypi.org/

# `pip` is the tool used to install packages:
#   Example (in terminal): `pip install cowsay`

# Once installed, you can import and use the package in your scripts.

import cowsay  # cowsay provides fun ASCII-art speech for various characters
import sys     # sys lets you interact with command-line arguments and the interpreter


def say():
    """
If the user provides one command-line argument,
print a greeting using the cow and T-Rex from cowsay.
    """
    if len(sys.argv) == 2:
        # Greet the user with a cow and a T-Rex ASCII art speech bubble
        cowsay.cow("hello, " + sys.argv[1])
        cowsay.trex("hello, " + sys.argv[1])


def main():
    # Entry point of the script
    say()


if __name__ == "__main__":
    # Ensures main() runs only when this file is executed directly
    main()

