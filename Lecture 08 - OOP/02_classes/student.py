# This script demonstrates how to define and use classes in Python.
# Classes allow you to create custom data types with attributes and behavior,
# following the principles of object-oriented programming (OOP).

import sys


# -----------------------------
# CLASS DEFINITION
# -----------------------------
class Student:
    """
Represents a Hogwarts student with a name, house, and patronus.

Attributes:
name (str): The student's name.
house (str): The Hogwarts house (must be one of four).
patronus (str): Optional magical protector (used for charm display).
"""

    def __init__(self, name=None, house=None, patronus=None):
        """
Constructor method, called when a new Student object is created.

Validates:
- 'name' must be provided.
- 'house' must be one of the four valid Hogwarts houses.
        """
        if not name:
            raise ValueError("Missing name")
        elif house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")

        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self) -> str:
        """
Returns a human-readable string representation of the student.
Called when you use print(student).
        """
        return f"{self.name} is in {self.house} and has a {self.charm()} patronus."

    def __repr__(self) -> str:
        """
Returns a detailed string useful for debugging.
Called by the built-in `repr()` function or in the console.
        """
        return f"Student({self.name}, {self.house}, {self.patronus})"

    def charm(self) -> str:
        """
Returns an emoji representation of the student's patronus.
        """
        match self.patronus:
            case "Stag":
                return "🦌"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🪄"  # default for unknown or missing patronus


# -----------------------------
# STUDENT INITIALIZATION METHODS
# -----------------------------

def get_student_variables():
    """
Less recommended: Create a student object with no arguments,
then assign values manually after creation.
    """
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


def get_student_constructor():
    """
Recommended: Prompt user for attributes before instantiating the Student.
Handles validation errors cleanly using try/except.
    """
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")

    try:
        return Student(name, house, patronus)  # Create and return the object
    except ValueError as e:
        sys.exit(e)  # Exit the program with error message if validation fails


# -----------------------------
# MAIN PROGRAM ENTRY POINT
# -----------------------------
def main():
    """
Main program function: prompts for student data and prints result.
Demonstrates the use of __str__ method automatically.
    """
    student = get_student_constructor()
    print(student)  # Calls student.__str__() implicitly


# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
    







