## Lecture 6 – File I/O

### Lists and Conventions
- **Lists** can store multiple variables or pieces of information in a single structure.  
- `_` (underscore) is often used as a Pythonic convention for variables that are intentionally unused.  

### File Handling in Python
- The `open()` function opens a file when given its filename. It can be used to read from or write to the file.  
- `'w'` opens a file for writing, overwriting its contents.  
- `'a'` opens a file for appending without removing existing contents.  
- `'r'` opens a file for reading.  
- Files should always be closed after writing or appending to them.  
- The `with` statement can be used to open a file and ensure it is automatically closed when finished.  

### Working with CSV Files
- **CSV files** (Comma-Separated Values) store data where values are separated by commas.  
- The `.split()` method, available to all strings, can split a string based on a given delimiter.  
- `DictReader` from the `csv` module can iterate over a CSV file, loading each line as a dictionary with keys based on column names.  

### Other Concepts
- A **lambda function** is an anonymous function — a function without a name — often used for short, simple operations.
