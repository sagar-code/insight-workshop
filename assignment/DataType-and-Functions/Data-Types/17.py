# 17. Write a Python program to multiplies all the items in a list.


# Get the input from the user
user_input = input("Enter the list of number to multiply. \n").split()
user_input_list = list(map(lambda x: int(x), user_input))

result = 1

for num in user_input_list:
    result *= num


print(result)