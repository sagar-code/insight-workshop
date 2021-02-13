# 4. Write a Python program to get a single string from two given strings, separated by a space and swap the first two
# characters of each string.

# Sample String: 'abc', 'xyz'
# Excepted Result: 'xycabz'


# Get the string from the user
first_string, second_string = input('Enter the two string separated by space. \n').split()

# swap the first two character of given strings
first_string_char = first_string[0: 2]
second_string_char = second_string[0: 2]

result = second_string_char + first_string[2:] + ' ' + first_string_char + second_string[2:]

print(result)