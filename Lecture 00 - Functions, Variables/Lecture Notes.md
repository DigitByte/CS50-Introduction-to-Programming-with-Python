# CS50P – Lecture Notes

This folder contains my personal notes from CS50P – Introduction to Programming with Python.  
Each lecture is documented with concise explanations, examples, and key takeaways.

---

## Lecture 0 – Functions and Variables

### Terminal and Functions
- **Terminal Window** – A command-line interface used to execute commands directly.  
- **Function** – An action that performs a specific task within a program.  
- **Arguments** – Inputs to a function that modify its behavior.  
- Functions can have **side effects** beyond returning a value.

### Programming Errors
- **Bug** – A mistake in a program that causes incorrect behavior and needs fixing.  
- **Syntax Error** – Mistakes in code structure or formatting, often caused by incorrect typing.

### Variables and Comments
- **Variable** – A container that stores a value.  
- **Comments** – Notes within the code that are ignored during execution; can be reminders or to-do items.  
- **Pseudocode** – A simplified, language-independent way to outline a program's logic.

### Data Types and String Operations
- **String (`str`)** – A sequence of characters.  
- `*objects` – The `print()` function can take multiple objects or strings as arguments.  
- `\n` – Creates a new line in output.  
- **`sep=' '`** – Default separator in `print()`, which adds a space between items.  
- **Positional arguments** – Values passed to a function in a specific order.  
- **Named parameters** – Specify values for parameters like `sep=' '` or `end=''`.  
- `\` – Escape character, used to represent special characters in strings.  
- `.strip()` – Removes leading and trailing whitespace from a string.  
- `.capitalize()` – Capitalizes the first letter of the first word in a string.  
- `.title()` – Capitalizes the first letter of each word in a string.  
- Method chaining is possible, e.g., `.strip().title()`.

### Numbers and Arithmetic
- **Integer (`int`)** – Whole numbers without decimals.  
- Arithmetic operators: `+`, `-`, `*`, `/`, `%`.  
- `int()` – Converts strings to integers for mathematical operations.  
- **Float (`float`)** – Numbers with decimal points.  
- `**` – Exponentiation (raising a number to a power).

### Functions and Scope
- `def` – Defines a new function.  
- **Scope** – The region of code where a variable is accessible.  
- `return` – Sends a value back from a function.

---

## Lecture 1 – Conditionals

### Scope
- Scope is the context in which a variable exists and can be accessed.
- Variables may not be accessible outside the scope in which they are created.

### Comparison Operators
Python provides several built-in comparison operators:
- `>` – Greater than  
- `>=` – Greater than or equal to  
- `<` – Less than  
- `<=` – Less than or equal to  
- `==` – Equal to (comparison)  
- `!=` – Not equal to  

### Boolean Expressions
- An expression like `x < y` evaluates to either `True` or `False`.
- Indentation determines which statements execute when a condition is met.

### Conditional Statements
- `if` – Executes a block of code if a condition is true.  
- `elif` – Short for *else if*; tests another condition if the previous one is false.  
- `else` – Executes a block of code when none of the preceding conditions are true.

### Logical Operators
- `or` – Returns `True` if at least one condition is true.  
- `and` – Returns `True` only if both conditions are true.  
- Useful for creating upper and lower bounds within conditions.

### Arithmetic and Modulus
- `%` (modulus) – Returns the remainder of a division operation.

### Boolean Values
- The `bool` data type represents only two values: `True` or `False`.

---

## Notes
- Fewer conditional blocks improve both efficiency and readability.
- Clear indentation and logical structure are essential for maintainable code.
