# 2. Write a Python function to sum all the number in the list.

# Sample List: [8, 2, 3, 0, 7]
# Excepted Output: 20


# Get the input from the user
user_input = input("Enter the list of number. \n").split(',')
user_input_integer = list(map(lambda x: int(x), user_input))


def sum_calc(list_):
    return sum(list_)


result = sum_calc(user_input_integer)
print(result)