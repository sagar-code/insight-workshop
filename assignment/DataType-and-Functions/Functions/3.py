# 3. Write a Python function to multiply all the numbers in the list.

# Sample List: [8, 2, 3, -1, 7]
# Excepted Output: -336


# Get the input from the user
user_input = input("Enter the list of number. \n").split(',')
user_input_integer = list(map(lambda x: int(x), user_input))


def mul_calc(list_):
    result = 1
    for num in list_:
        result *= num
    return result


output = mul_calc(user_input_integer)
print(output)
