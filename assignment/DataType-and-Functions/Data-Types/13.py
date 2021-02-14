# 13. Write a Python program to accepts a comma separated sequence of word as input and print out the unique words in
# sorted from (alphanumerically).

# Sample Words: red, white, black, red, green, black
# Excepted Result: black, green, red, white, red


# Get the input from the user
user_input = input("Enter the comma separated sequence of words. \n").split(',')

# program logic
result = sorted(set(user_input))
final_result = ','.join(result)
print(final_result)

