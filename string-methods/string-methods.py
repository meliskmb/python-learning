# 1. CASE CONVERSION
example = "hello world"

# Capitalize first letter, lowercase the rest
print("capitalize():", example.capitalize()) # Output: Hello world

# More aggressive lowercase conversion
print("casefold():", example.casefold())  # Output: hello world

# Convert to all lowercase
print("lower():", example.lower())  # Output: hello world

# Swap uppercase and lowercase.
print("swapcase():", example.swapcase())  # Output: HELLO WORLD

# Capitalize each word
print("title():", example.title())  # Output: Hello World

# Convert to all uppercase
print("upper():", example.upper())  # Output: HELLO WORLD

# 2. ALIGNMENT AND PADDING
example = "hello"

# Center the string in a field of the specified width
print("center(20):", example.center(20))  # Output: '       hello        '

# Left-justify the string in a field of the specified width
print("ljust(20):", example.ljust(20))  # Output: 'hello               '

# Right-justify the string in a field of the specified width
print("rjust(20):", example.rjust(20))  # Output: '               hello'

# Left-pad the string with zeros to reach the specified width
print("zfill(10):", example.zfill(10))  # Output: '00000hello'

# 3. SEARCHING
example = "hello world, hello Python"

# Count non-overlapping occurrences of a substring
print("count('hello'):", example.count('hello'))  # Output: 2

# Find the lowest index of the substring (-1 if not found)
print("find('world'):", example.find('world'))  # Output: 6

# Find the lowest index of the substring (raises ValueError if not found)
print("index('hello'):", example.index('hello'))  # Output: 0

# Find the highest index of the substring (-1 if not found)
print("rfind('hello'):", example.rfind('hello'))  # Output: 13

# Find the highest index of the substring (raises ValueError if not found)
print("rindex('hello'):", example.rindex('hello'))  # Output: 13