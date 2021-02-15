# 15. Write a Python program to filter a list of integer using Lambda.


# Get the input from the user
user_input = input("Enter the list of number. \n").split(',')
user_input_integer = list(map(lambda x: int(x), user_input))

# filter the list
even_number = list(filter(lambda x: x%2 == 0, user_input_integer))
print(even_number)

odd_number = list(filter(lambda x: x%2 !=0, user_input_integer))
print(odd_number)