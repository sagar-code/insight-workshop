# Write a Python program to remove the nth index character from a non-empty string.


# Get the input from the user
user_input = input("Enter the string. \n")
user_index = int(input("Enter the index number to remove. \n"))

# program logic
result = user_input[: user_index] + user_input[user_index + 1:]
print(result)