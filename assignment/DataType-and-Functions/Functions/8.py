# 8. Write a Python function that takes a list and return a new list with unique elements of the first list.

# Sample List: [1, 2, 3, 3, 3, 3, 4, 5]
# Unique List: [1, 2, ,3, 4, 5]


# Get the input from the user.
user_input = input("Enter the list item. \n").split()


def unique_list(list_):
    return list(set(list_))


result = unique_list(user_input)
print(result)