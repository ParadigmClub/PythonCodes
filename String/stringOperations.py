# len() - Returns the length of the string
example_str = "Hello, World!"
print(len(example_str))  # Output: 13

# count() - Returns the number of times substring occurs in the given string
print(example_str.count('o'))  # Output: 2

# split() - Breaks up a string at the specified separator and returns a list of substrings
print(example_str.split(','))  # Output: ['Hello', ' World!']

# capitalize() - Converts the first letter of the string to uppercase
print(example_str.capitalize())  # Output: 'Hello, world!'

# title() - Returns the string with the first letter of every word in uppercase and rest in lowercase
print(example_str.title())  # Output: 'Hello, World!'

# find() - Searches the first occurrence of the substring in the given string
print(example_str.find('World'))  # Output: 7

# replace() - Replaces all the occurrences of the old string with the new string
print(example_str.replace('World', 'Universe'))  # Output: 'Hello, Universe!'

# index() - Searches the first occurrence and returns the lowest index of the substring
print(example_str.index('World'))  # Output: 7

# lower() - Converts the string into lowercase
print(example_str.lower())  # Output: 'hello, world!'

# islower() - Returns True if all the letters in the string are in lowercase, otherwise False
print(example_str.islower())  # Output: False

# upper() - Converts the string into uppercase
print(example_str.upper())  # Output: 'HELLO, WORLD!'

# isupper() - Returns True if all the letters in the string are in uppercase, otherwise False
print(example_str.isupper())  # Output: False

# isalpha() - Checks for alphabets in an inputted string and returns True if the string contains only letters, else False
print("Hello".isalpha())  # Output: True

# isalnum() - Returns True if all the characters are alphanumeric, else False
print("Hello123".isalnum())  # Output: True

# isdigit() - Returns True if the string contains only digits, otherwise False
print("12345".isdigit())  # Output: True

# lstrip() - Returns the string after removing the space from the left of the string
print("   Hello".lstrip())  # Output: 'Hello'

# rstrip() - Returns the string after removing the space from the right of the string
print("Hello   ".rstrip())  # Output: 'Hello'

# strip() - Returns the string after removing the space from both sides of the string
print("   Hello   ".strip())  # Output: 'Hello'

# index() - Returns the index position of an element or an item in a string of characters or a list of items
print(example_str.index('World'))  # Output: 7

# startswith() - Returns True if the string starts with the given substring, and False otherwise
print(example_str.startswith('Hello'))  # Output: True

# partition() - Splits a given string into three parts based on the first occurrence of a specified separator
print(example_str.partition(','))  # Output: ('Hello', ',', ' World!')

# join() - Concatenates elements from an iterable (like a list or tuple) into a single string, with a specified separator between each element
print(', '.join(['apple', 'banana', 'cherry']))  # Output: 'apple, banana, cherry'

# endswith() - Returns True if the string ends with the given substring, and False otherwise
print(example_str.endswith('!'))  # Output: True