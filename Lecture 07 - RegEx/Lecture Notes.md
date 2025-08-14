## Lecture 7 – Regular Expressions

### Overview
- A **Regular Expression (regex)** is a pattern used to match specific types of data, such as user input. Regexes are commonly used for validation, for example ensuring that an integer is entered into an integer field.  
- The `.strip()` method can remove any leading or trailing whitespace from user input.  
- The `re` module provides functionality for working with regular expressions in Python. Documentation: [https://docs.python.org/3/library/re.html](https://docs.python.org/3/library/re.html)

### Common `re` Functions
- `re.search(pattern, string, flags=0)` – searches for a pattern in a string.  
- `re.sub(pattern, repl, string, count=0, flags=0)` – replaces occurrences of a pattern with a replacement string.

### Regex Symbols
- `.` – any character except a newline  
- `*` – 0 or more repetitions  
- `+` – 1 or more repetitions  
- `?` – 0 or 1 repetition  
- `{m}` – exactly m repetitions  
- `{m,n}` – between m and n repetitions  
- `^` – matches the start of a string  
- `$` – matches the end of a string just before a newline  
- `[]` – set of characters  
- `[^]` – complement of a set  
- `a-z` / `A-Z` – character ranges for lowercase or uppercase letters  
- `0-9` – numeric range  
- `\d` – decimal digit  
- `\D` – not a decimal digit  
- `\s` – whitespace character  
- `\S` – not a whitespace character  
- `\w` – word character (letters, numbers, underscore)  
- `\W` – not a word character  
- `A|B` – matches either A or B  
- `( … )` – grouping  
- `(?: … )` – non-capturing group  

### Additional Concepts
- **Flags** in `re` are configuration options that modify pattern matching behavior.  
- `:=` (walrus operator) allows assignment within expressions, often used in `if` conditions.
