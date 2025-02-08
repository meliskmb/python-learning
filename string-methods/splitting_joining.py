example = "hello world example"

# Joins iterable elements with a string separator
words = ["hello", "world", "Python"]
print("join():", " ".join(words))  # Output: 'hello world Python'

# join() with different separators
print("join with '-':", "-".join(words))  # Output: 'hello-world-Python'
print("join with '*':", "*".join("hello"))  # Output: 'h*e*l*l*o'

# Splits string into three parts: before, separator, after
print("partition('world'):", example.partition("world"))  # Output: ('hello ', 'world', ' example')

# partition() when separator is not found
print("partition('notfound'):", example.partition("notfound"))  # Output: ('hello world example', '', '')

# Splits from the rightmost occurrence of the separator
print("rpartition('world'):", example.rpartition("world"))  # Output: ('hello ', 'world', ' example')

# rpartition() when separator is not found
print("rpartition('notfound'):", example.rpartition("notfound"))  # Output: ('', '', 'hello world example')

# Splits string into a list using a separator (default: whitespace)
print("split():", example.split())  # Output: ['hello', 'world', 'example']

# split() with a specific separator
csv_data = "apple,banana,grape"
print("split(','):", csv_data.split(","))  # Output: ['apple', 'banana', 'grape']

# split() with maxsplit argument
print("split(' ', 1):", example.split(" ", 1))  # Output: ['hello', 'world example']

# Splits from the right side, optional max splits
print("rsplit(' ', 1):", example.rsplit(" ", 1))  # Output: ['hello world', 'example']

# rsplit() with multiple splits
long_text = "one two three four five"
print("rsplit(' ', 2):", long_text.rsplit(" ", 2))  # Output: ['one two three', 'four', 'five']

# Splits on newline characters
multiline = "Hello\nWorld\nPython"
print("splitlines():", multiline.splitlines())  # Output: ['Hello', 'World', 'Python']

# splitlines(True) keeps newline characters
print("splitlines(True):", multiline.splitlines(True))  # Output: ['Hello\n', 'World\n', 'Python']