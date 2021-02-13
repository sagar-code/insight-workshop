# Write a Python program to get a string from a given string where all occurrences of its first char have been changed
# to '$', except the first char itself.

# Sample String: 'restart'
# Excepted Result: 'resta$t'


# Get the user input
user_input = input("Enter the string: \n")

# program logic
result = user_input[1:].replace(user_input[0], '$')

final_result = user_input[0] + result

print(final_result)