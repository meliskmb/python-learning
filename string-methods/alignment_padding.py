example = "hello"

# Center the string in a field of the specified width (default padding with spaces)
print("center(20):", example.center(20))  # Output: '       hello        '

# Center with a custom fill character
print("center(20, '*'):", example.center(20, '*'))  # Output: '*******hello*******'

# Left-justify the string in a field of the specified width
print("ljust(20):", example.ljust(20))  # Output: 'hello               '

# Left-justify with a custom fill character
print("ljust(20, '-'):", example.ljust(20, '-'))  # Output: 'hello---------------'

# Right-justify the string in a field of the specified width
print("rjust(20):", example.rjust(20))  # Output: '               hello'

# Right-justify with a custom fill character
print("rjust(20, '#'):", example.rjust(20, '#'))  # Output: '###############hello'

# Left-pad the string with zeros to reach the specified width
print("zfill(10):", example.zfill(10))  # Output: '00000hello'

# zfill applied to a string with a negative sign
negative_example = "-42"
print("zfill(5) with negative number:", negative_example.zfill(5))  # Output: '-0042'

# Handling cases where the width is less than the string length
print("center(3):", example.center(3))  # Output: 'hello' (no change, as width < len(string))
print("ljust(3):", example.ljust(3))    # Output: 'hello' (no change)
print("rjust(3):", example.rjust(3))    # Output: 'hello' (no change)
print("zfill(3):", example.zfill(3))    # Output: 'hello' (no change)