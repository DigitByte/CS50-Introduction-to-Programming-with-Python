# Tuples are immutable sequences; elements can be accessed by index
def get_student_tuple():
    name = input("Name: ")
    house = input("House: ")

    return (name, house)  # parentheses optional for tuple


# Lists are mutable and also indexable
def get_student_list():
    name = input("Name: ")
    house = input("House: ")

    return [name, house]  # list allows modification


# Dictionaries use key-value pairs; better for labeled data
def get_student_dict():
    name = input("Name: ")
    house = input("House: ")

    return {
        "name": name,
        "house": house,
    }


def main():
    student = get_student_dict()  # returns dictionary with clear keys
    # print(f"{student[0]} is in {student[1]}")  # would work with list/tuple
    print(f"{student['name']} is in {student['house']}")  # dictionary access


if __name__ == "__main__":
    main()
    