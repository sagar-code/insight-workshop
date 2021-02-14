# 18. Write a Python program to get the largest number from a list.


# Get the input from the user.
user_input = input("Enter the list of number. \n").split()
user_input_integer = list(map(lambda x: int(x), user_input))

# largest number finding logic
result = 0

for num in user_input_integer:
    if num > result:
        result = num

print(result)