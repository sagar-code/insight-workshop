# 16. Write a Python program to square and cube every number in a given list of integers using Lambda.


# Get the input from the user
user_input = input("Enter the list of number. \n").split(',')
user_input_integer = list(map(lambda x: int(x), user_input))

# lambda function
square_list = list(map(lambda x: x ** 2, user_input_integer))
cube_list = list(map(lambda x: x ** 3, user_input_integer))

print(square_list)
print(cube_list)