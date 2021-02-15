# 20. Write a Python program to find intersection of two given arrays using Lambda.

# Get the input from the user
user_input = input("Enter the first list of number. \n").split(',')
user_input_integer_1 = list(map(lambda x: int(x), user_input))

user_input_2 = input("Enter the first list of number. \n").split(',')
user_input_integer_2 = list(map(lambda x: int(x), user_input_2))

# intersection using lambda
result = list(filter(lambda x: x in user_input_integer_1, user_input_integer_2))
print(result)