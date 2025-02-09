# Removes leading and trailing whitespace or specified characters
example = "   hello world   "
print("strip():", example.strip())  # Output: 'hello world'

# strip() with specific characters
example2 = "###hello world###"
print("strip('#'):", example2.strip("#"))  # Output: 'hello world'

# strip() with multiple characters and non-adjacent matches
example3 = "abc hello world abc"
print("strip('abc'):", example3.strip("abc"))  # Output: ' hello world ' (leading and trailing "abc" removed)

# strip() with a mix of spaces and characters
example4 = "   #hello world###   "
print("strip('# '):", example4.strip("# "))  # Output: 'hello world'

# Removes leading whitespace or specified characters
example5 = "   hello world   "
print("lstrip():", example5.lstrip())  # Output: 'hello world   '

# lstrip() with specific characters
example6 = "###hello world###"
print("lstrip('#'):", example6.lstrip("#"))  # Output: 'hello world###'

# lstrip() with multiple characters
example7 = "****hello world"
print("lstrip('*'):", example7.lstrip("*"))  # Output: 'hello world'

# Removes trailing whitespace or specified characters
example8 = "   hello world   "
print("rstrip():", example8.rstrip())  # Output: '   hello world'

# rstrip() with specific characters
example9 = "hello world###"
print("rstrip('#'):", example9.rstrip("#"))  # Output: 'hello world'

# rstrip() with multiple characters
example10 = "hello world****"
print("rstrip('*'):", example10.rstrip("*"))  # Output: 'hello world'

# lstrip(), rstrip() with characters example
example11 = "***hello world***"
print("lstrip('*'):", example11.lstrip("*"))  # Output: 'hello world***'
print("rstrip('*'):", example11.rstrip("*"))  # Output: '***hello world'

# strip() with multiple characters, handling non-adjacent matches
example12 = "xxxyyyhello worldzzz"
print("strip('xyz'):", example12.strip("xyz"))  # Output: 'hello world'

# strip() to remove whitespace and specific characters from both ends
example13 = "!!!hello world   "
print("strip('! '):", example13.strip("! "))  # Output: 'hello world'