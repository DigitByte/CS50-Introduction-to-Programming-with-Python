# This script demonstrates how to use Python's "re" (regular expressions) module
# to validate email addresses using various levels of pattern strictness.

import re


# --- REGEX MODULE OVERVIEW ---
# The "re" module in Python allows you to work with **regular expressions (regex)**—
# powerful patterns used for string matching, searching, splitting, and replacing.

# Common use cases include:
# - Validating user input (e.g., email addresses, phone numbers)
# - Searching within text
# - Extracting or replacing substrings

# ----------------------
# SPECIAL REGEX CHARACTERS
# ----------------------
# .         Matches any character except a newline
# *         Matches 0 or more repetitions
# +         Matches 1 or more repetitions
# ?         Matches 0 or 1 repetition (optional)
# {m}       Exactly m repetitions
# {m,n}     Between m and n repetitions
# ^         Matches the start of the string
# $         Matches the end of the string
# []        Matches a set of characters (e.g., [a-z])
# [^]       Matches any character not in the set
# \d        Matches a digit (0–9)
# \D        Matches a non-digit
# \s        Matches any whitespace character
# \S        Matches any non-whitespace character
# \w        Matches any alphanumeric character or underscore
# \W        Matches any non-word character
# A|B       Matches either A or B
# (...)     Groups expressions (captures the matched text)
# (?:...)   Groups expressions but does NOT capture the match (non-capturing group)

# ----------------------
# FUNCTION: Basic Email Check
# ----------------------
def simple_check(email):
    """
Checks if the email contains:
- At least one character, then '@'
- At least one character, then '.'
- At least one character

Example valid: someone@example.com
Example invalid: foo@@bar.com, foo.com, @bar.com
    """
    if re.search(r".+@.+\..+", email):  # raw string to prevent escape issues
        return True
    return False


# ----------------------
# FUNCTION: Slightly Stricter Check
# ----------------------
def simple_check1(email):
    """
Enforces:
- No '@' symbols before or after the main '@'
- Ends in .edu
- No spaces

Example valid: user@domain.edu
Example invalid: edu@domain.edu, user@domain.edu.edu
    """
    if re.search(r"^[^@]+@[^@]+\.edu$", email):
        return True
    return False


# ----------------------
# FUNCTION: Tighter Pattern with Character Constraints
# ----------------------
def final_check_long(email):
    """
Accepts only:
- Letters, digits, dots, and underscores before '@'
- Letters and dots in the domain
- Must end with '.edu'
    """
    if re.search(r"^[a-zA-Z0-9._]+@[a-zA-Z0-9.]+\.edu$", email):
        return True
    return False


# ----------------------
# FUNCTION: Support for Multiple Domains
# ----------------------
def final_check_almost(email):
    """
Accepts:
- Usernames and domains with word characters (letters, digits, underscores)
- Accepts .com, .org, .edu, .it domains
- Case-sensitive: will fail if domain is uppercase
    """
    if re.search(r"^[\w.]+@[\w.]+\.(com|it|org|edu)$", email):
        return True
    return False


# ----------------------
# FUNCTION: Case-Insensitive Domain Matching
# ----------------------
def final_check_maybe(email):
    """
Improves the previous function by adding case insensitivity using re.IGNORECASE.
Still allows invalid formats like ......@.....edu
    """
    if re.search(r"^[\w.]+@[\w.]+\.(com|it|org|edu)$", email, re.IGNORECASE):
        return True
    return False


# ----------------------
# FUNCTION: Final, RFC-5322-Compliant-ish Email Check
# ----------------------
def final_check(email):
    """
A more robust regex for email validation that:
- Allows valid characters in the username
- Accepts hyphenated domain names
- Prevents invalid formats like consecutive dots or trailing '@'

Note: Still not 100% RFC-compliant (use a library like `validate_email` for that),
but this is good enough for general-purpose validation.
    """
    if re.search(
        r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+"
        r"@"
        r"[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?"
        r"(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$",
        email,
        re.IGNORECASE,
    ):
        return True
    return False


# ----------------------
# MAIN EXECUTION
# ----------------------
def main():
    """
Ask the user to enter an email and validate it using the final_check function.
    """
    email = input("What's your email address? ").strip()

    if final_check(email):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()


# ----------------------
# ADDITIONAL NOTES
# ----------------------
# re.search(pattern, string, flags=0)    -> Searches for the pattern anywhere in the string
# re.match(pattern, string, flags=0)     -> Matches the pattern only at the beginning
# re.fullmatch(pattern, string, flags=0) -> Matches the entire string (start to end)

# Pro Tip:
# For production-level email validation, it’s best to use a well-maintained package
# like `email-validator`, which handles all edge cases and RFC rules.
