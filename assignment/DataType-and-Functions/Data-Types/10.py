# 10. Write a Python program to remove the characters which have odd index values of a given string.


# Get the input from the user
user_input = input("Enter the string. \n")

result = ''.join([s for i, s in enumerate(user_input, 1) if i % 2 == 0])
print(result)