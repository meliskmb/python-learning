example = "hello world, hello Python"
case_sensitive_example = "Hello hello HELLO"
special_chars = "hello@world! hello#Python"
numbers_example = "abc123 abc456 abc123"

# Count non-overlapping occurrences of a substring
print("count('hello'):", example.count('hello'))  # Output: 2
print("count('Hello') (case-sensitive):", case_sensitive_example.count('Hello'))  # Output: 1
print("count('abc123'):", numbers_example.count('abc123'))  # Output: 2

# Find the lowest index of the substring (-1 if not found)
print("find('world'):", example.find('world'))  # Output: 6
print("find('Python'):", example.find('Python'))  # Output: 19
print("find('not_found'):", example.find('not_found'))  # Output: -1
print("find('@'):", special_chars.find('@'))  # Output: 5
print("find('hello', 10):", example.find('hello', 10))  # Output: 13 (Only search after index 10)

# Find the lowest index of the substring (raises ValueError if not found)
print("index('hello'):", example.index('hello'))  # Output: 0
# print("index('not_found'):", example.index('not_found'))  # Raises ValueError

# Find the highest index of the substring (-1 if not found)
print("rfind('hello'):", example.rfind('hello'))  # Output: 13
print("rfind('not_found'):", example.rfind('not_found'))  # Output: -1
print("rfind('Python'):", example.rfind('Python'))  # Output: 19
print("rfind('#'):", special_chars.rfind('#'))  # Output: 18
print("rfind('hello', 0, 10):", example.rfind('hello', 0, 10))  # Output: 0 (Only search within range)

# Find the highest index of the substring (raises ValueError if not found)
print("rindex('hello'):", example.rindex('hello'))  # Output: 13
# print("rindex('not_found'):", example.rindex('not_found'))  # Raises ValueError

# Check if the string starts with a specific prefix
print("startswith('hello'):", example.startswith("hello"))  # Output: True
print("startswith('world'):", example.startswith("world"))  # Output: False
print("startswith(('hi', 'hello')):", example.startswith(("hi", "hello")))  # Output: True
print("startswith('hello', 7):", example.startswith("hello", 7))  # Output: False

# Check if the string ends with a specific suffix
print("endswith('Python'):", example.endswith("Python"))  # Output: True
print("endswith('hello'):", example.endswith("hello"))  # Output: False
print("endswith(('world', 'Python')):", example.endswith(("world", "Python")))  # Output: True
print("endswith('Python', 0, 25):", example.endswith("Python", 0, 25))  # Output: True