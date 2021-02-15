# 10. Write a Python program to print the even numbers from a given list.

# Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Excepted Result: [2, 4, 6, 8]

# Get the input from the user
user_input = input("Enter the list of number. \n").split(',')
user_input_integer = list(map(lambda x: int(x), user_input))


def check_even(list_):
    result = []
    for i in list_:
        if i % 2 == 0:
            result.append(i)

    return result


output = check_even(user_input_integer)
print(output)