example1 = "HelloWorld123"  # Alphanumeric
example2 = "HelloWorld"  # Alphabetic only
example3 = "123"  # Digits only
example4 = "  "  # Whitespace only
example5 = "π"  # Unicode character
example6 = "hello"  # Lowercase
example7 = "HELLO"  # Uppercase
example8 = "Hello World"  # Title case
example9 = "Hello\nWorld"  # Contains newline

# Checks if all characters are alphanumeric (letters and numbers only)
print("isalnum():", example1.isalnum())  # Output: True

# Checks if all characters are alphabetic (letters only)
print("isalpha():", example2.isalpha())  # Output: True

# Checks if all characters are ASCII (0-127)
print("isascii():", example1.isascii())  # Output: True
print("isascii() with π:", example5.isascii())  # Output: False

# Checks if all characters are decimal numbers (0-9 only)
print("isdecimal():", example3.isdecimal())  # Output: True
print("isdecimal() with π:", example5.isdecimal())  # Output: False

# Checks if all characters are digits (includes Unicode numbers)
print("isdigit():", example3.isdigit())  # Output: True
print("isdigit() with π:", example5.isdigit())  # Output: False

# Checks if all characters are numeric (includes fractions, subscripts, etc.)
print("isnumeric():", example3.isnumeric())  # Output: True
print("isnumeric() with π:", example5.isnumeric())  # Output: False

# Checks if the string is a valid Python variable name
print("isidentifier():", "my_variable".isidentifier())  # Output: True
print("isidentifier() with 123var:", "123var".isidentifier())  # Output: False

# Checks if all characters are lowercase
print("islower():", example6.islower())  # Output: True
print("islower() with Hello:", "Hello".islower())  # Output: False

# Checks if all characters are uppercase
print("isupper():", example7.isupper())  # Output: True
print("isupper() with Hello:", "Hello".isupper())  # Output: False

# Checks if the string follows title case (each word capitalized)
print("istitle():", example8.istitle())  # Output: True
print("istitle() with hello World:", "hello World".istitle())  # Output: False

# Checks if all characters are printable (no control characters like \n, \t)
print("isprintable():", example8.isprintable())  # Output: True
print("isprintable() with newline:", example9.isprintable())  # Output: False

# Checks if all characters are whitespace (spaces, tabs, newlines)
print("isspace():", example4.isspace())  # Output: True
print("isspace() with 'Hello':", "Hello".isspace())  # Output: False