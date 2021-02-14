# 26. Write a Python program to insert a given string at the beginning of all items in a list.

# Sample List: [1, 2, 3, 4], String: emp
# Excepted Output: ['emp1', 'emp2', 'emp3', 'emp4']


# Get the input from the user
user_list = input("Enter the list of integer. \n").split()
user_string = input("Enter the string. \n")

# program logic
result = [user_string+i for i in user_list]
print(result)
