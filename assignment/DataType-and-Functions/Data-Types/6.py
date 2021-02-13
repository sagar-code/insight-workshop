# 6. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not'
# follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

# Sample String: 'The lyrics is not that poor!'
# Excepted Result: 'The lyrics is good!'

# Sample String: 'The lyrics is poor!'
# Excepted Result: 'The lyrics is poor!'


# Get the input from the user
user_input = input("Enter the string: \n")

# find the index of not and poor
not_index = user_input.find('not')
poor_index = user_input.find('poor')

if (not_index < poor_index) and (poor_index > 0) and (not_index > 0):
    result = user_input.replace(user_input[not_index: poor_index+4], 'good')
    print(result)
else:
    print(user_input)

