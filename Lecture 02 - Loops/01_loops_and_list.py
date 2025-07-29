#############################################################
#                           Loops                           #
#############################################################
# loops are a way to do something over and over again.

# While loop example: simple countdown
def cat():
    n = int(input("How many cats do you have? "))

    while n > 0:
        print("Meow")
        n -= 1


# For loop using a list or a range
def cat_list():
    n = int(input("How many cats do you have? "))

    for _ in range(n):  # range(n) generates 0 to n-1
        print("Meow")


# Pythonic one-liner using string multiplication
def cat_pythonic():
    n = int(input("How many cats do you have? "))
    print("Meow\n" * n, end="")  # end="" avoids extra newline


# Loop with input validation
def cat_correct():
    while True:
        n = int(input("How many cats do you have? "))
        if n > 0:
            break

    for _ in range(n):
        print("Meow")


# Reusable input validation function
def get_number():
    while True:
        n = int(input("What's n? "))
        if n >= 0:
            return n


# Function calling a validated number and printing meows
def meow():
    for _ in range(get_number()):
        print("meow")


#############################################################
#                          Lists                            #
#############################################################

# Iterating over a list of students
def hogwarts():
    students = ["Hermonie", "Harry", "Ron", "Draco", "Luna", "Neville"]

    for student in students:  # Directly looping through list
        print(student)

    # Using range and len() to access index + value
    for i in range(len(students)):
        print(i + 1, students[i])  # Print position (1-based) and name


# Run the list example
hogwarts()
