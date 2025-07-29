#############################################################
#                          Random                           #
#############################################################

# The `random` module provides functions for generating random numbers
# and performing random operations on sequences.

# Importing the whole module allows access to all its functions with the module prefix.
import random

# Alternatively, specific functions can be imported directly using `from`.
from random import choice  # Enables calling `choice()` directly without prefix.

# Note: importing functions directly may cause naming conflicts if function names overlap.


def flip_coin():
    """
Simulate flipping a coin by randomly choosing between "heads" and "tails".
Uses random.choice(seq), which returns a random element from the sequence.
    """
    return random.choice(["heads", "tails"])


def randint(a, b):
    """
Return a random integer N such that a <= N <= b.
random.randint(a, b) includes both endpoints with equal probability.
    """
    return random.randint(a, b)  # Function name intentionally same as module's


def shuffle(lst):
    """
Shuffle a list in place, randomly reordering its elements.
random.shuffle(lst) modifies the list directly and returns None.
    """
    random.shuffle(lst)


def main():
    print(flip_coin())  # Prints "heads" or "tails"
    print(randint(1, 10))  # Prints a random integer between 1 and 10 (inclusive)

    cards = ["jack", "queen", "king", "ace"]
    shuffle(cards)  # Cards list is shuffled in place
    print(cards)  # Prints the shuffled list


if __name__ == "__main__":
    # Standard boilerplate to run main() only when script is executed directly
    main()
    