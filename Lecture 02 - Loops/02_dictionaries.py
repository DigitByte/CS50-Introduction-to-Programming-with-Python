#############################################################
#                        Dictionaries                       #
#############################################################

# Dictionary: { key : value } pairs
def hogwarts():
    # Correspondence using two separate lists (not ideal)
    students = ["Hermione", "Harry", "Ron", "Draco"]
    houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

    # This method does not scale well and is prone to mismatch

    # Better approach: use a dictionary to associate names with houses
    students = {
        "Hermione": "Gryffindor",
        "Harry": "Gryffindor",
        "Ron": "Gryffindor",
        "Draco": "Slytherin",
    }

    for student in students:
        # Iterates through the keys (student names) to access values
        print(student, "is in", students[student])


# List of dictionaries — more structured data
def hogwarts_patronus():
    students = [
        {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
        {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
        {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
        {"name": "Draco", "house": "Slytherin", "patronus": None},  # None = no value (like undefined in JS)
    ]

    for student in students:
        # Access and print multiple fields using dictionary keys
        print(student["name"], student["house"], student["patronus"], sep=" - ")


# Run the structured dictionary example
hogwarts_patronus()
