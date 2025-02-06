example = "hello world"
mixed_case = "PyThOn PrOgRaMmIng"
special_chars = "çağrı Ünlü Straße"
numbers_and_symbols = "hello123! WORLD"
unicode_example = "Γειά Σου Κόσμε"  # Greek
title_mixed = "this is an exAmple title"

# Capitalize first letter, lowercase the rest
print("capitalize():", example.capitalize())  # Output: Hello world

# More aggressive lowercase conversion (useful for non-English characters)
print("casefold():", special_chars.casefold())  # Output: çağrı ünlü strasse
print("casefold() with ß:", "Straße".casefold())  # Output: strasse

# Convert to all lowercase
print("lower():", mixed_case.lower())  # Output: python programming
print("lower() with Unicode:", unicode_example.lower())  # Works with Greek: γειά σου κόσμε

# Swap uppercase and lowercase
print("swapcase():", mixed_case.swapcase())  # Output: pYtHoN pRoGrAmMiNG
print("swapcase() with special chars:", special_chars.swapcase())  # Output: ÇAĞRI üNLÜ sTRASSE

# Capitalize each word
print("title():", example.title())  # Output: Hello World
print("title() with mixed case:", title_mixed.title())  # Output: This Is An Example Title

# Convert to all uppercase
print("upper():", numbers_and_symbols.upper())  # Output: HELLO123! WORLD
print("upper() with Unicode:", unicode_example.upper())  # Output: ΓΕΙΆ ΣΟΥ ΚΌΣΜΕ