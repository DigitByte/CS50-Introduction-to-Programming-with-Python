def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check length (2–6 chars) and starts with 2 letters
    if not 2 <= len(s) <= 6 or not s[:2].isalpha():
        return False

    # Must be alphanumeric (no punctuation or spaces)
    elif not s.isalnum():
        return False

    else:
        # Check rules for numbers if they appear
        sub = s[2:]  # only check the rest after the first 2 letters
        for i in range(len(sub)):
            if sub[i].isdigit():
                # First number must not be '0' and rest must be only digits
                if sub[i] == "0" or not sub[i:].isdigit():
                    return False
                else:
                    return True
        return True  # no numbers found → valid


if __name__ == "__main__":
    main()
