# 5. Write a Python program to add 'ing' at the end of a string (length should be at least 3). If the given string is
# already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it
# unchanged.

# Sample String: 'abc'
# Excepted Result: 'abcing'

# Sample String: 'string'
# Excepted Result: 'stringly'


# Get the input from the user
user_input = input('Enter the string. \n')

result = ''

# logic for the program
if len(user_input) >= 3:
    if user_input.endswith('ing'):
        result = user_input + 'ly'
    else:
        result = user_input + 'ing'
else:
    result = user_input


print(result)
