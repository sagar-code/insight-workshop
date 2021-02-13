# 9. Write a Python program to change a given string to a new string where the first and last chars have been
# exchanged.


# Get the input from the user
user_input = input("Enter the string: \n")

# program logic
first_char, last_char = user_input[-1], user_input[0]

result = first_char + user_input[1: -1] + last_char
print(result)