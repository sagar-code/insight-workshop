# 19. Write a Python program to get the smallest number from a list.


# Get the input from the user
user_input = input("Enter the list of number. \n").split()
user_input_integer = list(map(lambda x: int(x), user_input))

# sort the user input integer
user_input_integer.sort()

result = user_input_integer[0]
print(result)