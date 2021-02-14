# 22. Write a Python program to remove the duplicates from a list.


# Get the input from the user
user_input = input("Enter the list item. \n").split()

# remove a duplicate item from a list
result = list(set(user_input))
print(result)