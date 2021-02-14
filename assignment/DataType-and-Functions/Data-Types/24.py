# 24. Write a Python program to clone or copy a list.


# import the copy module
import copy

# Get the input form the user
user_input = input("Enter a list to copy. \n")

# logic
new_copy = copy.deepcopy(user_input)

print(f"Original list: {user_input}")
print(f"Copy List: {new_copy}")