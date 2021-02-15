# 27. Write a Python program to replace the last element in a list with another list.

# Sample Data: [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Excepted Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]


# Get the input from the user
first_data = input("Enter the list of data. \n").split()
first_data_integer = list(map(lambda x: int(x), first_data))

second_data = input("Enter the second data. \n").split()
second_data_integer = list(map(lambda x: int(x), second_data))

# program logic
first_data_integer[-1: ] = second_data_integer

print(first_data_integer)