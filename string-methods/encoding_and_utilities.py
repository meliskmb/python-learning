example = "hello world"

# Converts a string into bytes using different encodings
utf8_encoded = example.encode("utf-8")
print("encode('utf-8'):", utf8_encoded)  # Output: b'hello world'

utf16_encoded = example.encode("utf-16")
print("encode('utf-16'):", utf16_encoded)  # Output: b'\xff\xfeh\x00e\x00l\x00l\x00o\x00 ...'

latin1_encoded = example.encode("latin-1")
print("encode('latin-1'):", latin1_encoded)  # Output: b'hello world'

# Encoding with error handling
# print("hello 😊".encode("ascii"))  # Error: UnicodeEncodeError
print("encode('ascii', 'ignore'):", "hello 😊".encode("ascii", "ignore"))  # Output: b'hello '
print("encode('ascii', 'replace'):", "hello 😊".encode("ascii", "replace"))  # Output: b'hello ?'

# Expands tab characters ('\t') into spaces
tabbed_string = "hello\tworld\tPython"
print("expandtabs(4):", tabbed_string.expandtabs(4))  # Output: 'hello   world   Python'
print("expandtabs(8):", tabbed_string.expandtabs(8))  # Output: 'hello   world   Python'
print("expandtabs(2):", tabbed_string.expandtabs(2))  # Output: 'hello world Python'

# Formats a string using placeholders
print("format():", "My name is {}".format("Alice"))  # Output: My name is Alice
print("format() with multiple values:", "{} + {} = {}".format(3, 2, 3 + 2))  # Output: 3 + 2 = 5
print("format() with named arguments:", "Hello {name}".format(name="Bob"))  # Output: Hello Bob

# format() with positional and keyword arguments
print("format() mixed:", "{0} is learning {lang}".format("Alice", lang="Python"))  # Output: Alice is learning Python

# format() using f-string (Python 3.6+)
name, age = "Charlie", 25
print(f"f-string: My name is {name} and I am {age} years old")  # Output: My name is Charlie and I am 25 years old

# Similar to format(), but takes a dictionary as input
person = {"name": "Charlie", "age": 25}
print("format_map():", "My name is {name} and I am {age} years old".format_map(person)) # Output: My name is Charlie and I am 25 years old

# format_map() with defaultdict to handle missing keys
from collections import defaultdict
person_data = defaultdict(lambda: "Unknown", name="Dana")
print("format_map() with defaultdict:", "My name is {name} and I am {age} years old".format_map(person_data)) # Output: My name is Dana and I am Unknown years old
