# Goal: Prompt the user for the URL of their Twitter profile
# and extract the username from the URL using regular expressions.

import re


def main():
    """
Main function that prompts the user for their Twitter profile URL
and prints the extracted username, if valid.
    """
    url = input("Twitter profile URL: ").strip()
    handle = username(url)

    if handle:
        print(f"Username: {handle}")
    else:
        print("Invalid Twitter URL")


# ----------------------
# VARIOUS EXTRACTION METHODS
# ----------------------

def username_group(url):
    """
Extracts the username using a basic capturing group.
Assumes the URL contains 'twitter.com/username'.
Does not validate full URL structure.
    """
    return re.search(r"twitter.com/(\w+)/?", url).group(1)


def username_sub(url):
    """
Removes the protocol and domain part of the Twitter URL using substitution.
Returns the remaining string, which should be the username (but may contain extra path segments).
    """
    return re.sub(r"(https?://)?(www\.)?twitter\.com/", "", url, flags=re.IGNORECASE)


def username_groups(url):
    """
Uses the walrus operator (Python 3.8+) to extract the username from a full Twitter URL
with optional protocol and 'www'. Uses capturing group #3.
    """
    if matches := re.search(r"^(https?://)?(www\.)?twitter\.com/(\w+)/?", url, re.IGNORECASE):
        return matches.group(3)
    else:
        return ""


def username(url):
    """
Final version: extracts the username from a Twitter URL using non-capturing groups
for the protocol and subdomain, and a capturing group for the actual username.
Case-insensitive and ignores trailing slashes.
    """
    if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(\w+)/?", url, re.IGNORECASE):
        return matches.group(1)
    else:
        return ""


# Entry point
if __name__ == "__main__":
    main()
    