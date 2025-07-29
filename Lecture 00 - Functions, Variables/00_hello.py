#############################################################
#                           Hello!                          #
#############################################################

# Ask user for their name
name = input("Hello, friend. What is your name? ")  # input gets a string from stdio and stores it in a variable

# Say hello to the user
print("hello, " + name)  # String concatenation
print("hello,", name)    # Multiple arguments to print() lead to automatic space addition


"""
Named Parameters in print()
---------------------------
According to the Python documentation, the print() function is defined as:
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

This means:
- It can take multiple objects (separated by commas)
- Optional *named parameters* can be passed:
• sep: defines the separator between objects (default is a space)
• end: defines what to print at the end (default is a newline '\n')
• file and flush control output and buffering

Examples below demonstrate overriding these named parameters.
"""
print("hello, ", end="")  # Prevents a newline after this print
print(name)               # Continues on the same line

print("hello,", name, sep="_")  # Changes the default separator from space to underscore


# Demonstrating quotes inside strings
print('hello, "friend" or...', 'hello, "friend"')  # Both use single quotes to include double quotes inside strings


# Special Strings: f-strings (formatted strings)
# f-strings are prefixed with 'f' and allow you to embed expressions inside curly braces {}
print(f"hello, {name}")  # This is often preferred for cleaner and more readable code


#############################################################
#                       String Methods                      #
#############################################################
# A string, known as a str in Python, is a sequence of text.

# Original string with unwanted whitespaces
name = "     damien   delgado   "

# String methods:
name = name.strip()        # Removes leading/trailing whitespace characters
name = name.capitalize()   # Capitalizes the first character; lowers the rest
print(f"hello, {name}")

name = name.title()        # Capitalizes each word (title-style)
print(f"hello, {name}")


# Function Chaining:
# Methods can be chained to process input in one line
name = input("What is your name bro?\n").strip().title()
print(f"Hello, {name}")


# Splitting Strings:
# split() splits a string by whitespace by default and returns a list
# Unpacking the result into two variables assumes two words are entered
first_name, last_name = name.split(" ")
print(f"Hello, {first_name}")
