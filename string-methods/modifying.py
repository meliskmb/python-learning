example = "hello world"

# Replaces a substring with another substring
print("replace():", example.replace("world", "Python"))  # Output: hello Python

# Removes a specified prefix (Python 3.9+)
example_prefix = "HelloPython"
print("removeprefix():", example_prefix.removeprefix("Hello"))  # Output: Python

# Removes a specified suffix (Python 3.9+)
example_suffix = "PythonWorld"
print("removesuffix():", example_suffix.removesuffix("World"))  # Output: Python

# maketrans() - Creates a translation table for character replacement
# str.maketrans("karakterler", "yerine_geçecekler") şeklinde kullanılır
# Burada: 'a' -> '1', 'e' -> '2', 'i' -> '3', 'o' -> '4', 'u' -> '5' olarak değiştirilir.
vowel_translation = str.maketrans("aeiou", "12345")  # Replace vowels with numbers
print("maketrans() + translate():", "hello".translate(vowel_translation))  # Output: h2ll4

# maketrans() with dictionary - Replace multiple characters
# Burada bir sözlük kullanarak belirli harfleri değiştirebiliriz.
# 'h' büyük 'H' olur, 'w' büyük 'W' olur.
custom_table = str.maketrans({"h": "H", "w": "W"})
print("translate() with dict:", example.translate(custom_table))  # Output: Hello World

# maketrans() with removal - Removes characters using None
# Burada "aeiou" harflerini None'a eşleyerek kaldırıyoruz.
remove_table = str.maketrans("", "", "aeiou")  # Remove vowels
print("translate() for removal:", "hello world".translate(remove_table))  # Output: hll wrld