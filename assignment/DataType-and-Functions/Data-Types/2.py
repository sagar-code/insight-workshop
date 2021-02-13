# 2. Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. If the string
# length is less than 2, return instead of the empty string.

# Sample String: 'Python'
# Expected Result: 'Pyon'

# Sample String: 'Py'
# Expected Result: 'PyPy'

# Sample String: 'w'
# Expected Result: Empty String


# Get the input of string from the user
user_input = input("Enter a string. \n")

# logic to get the string for first and last two item
result = []

if len(user_input) >= 2:
    result.append(user_input[0] + user_input[1] + user_input[-2] + user_input[-1])

else:
    result = 'Empty String'

final_result = ''.join(result)
print(final_result)

