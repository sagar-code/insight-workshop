# 16. Write a Python program to sum all the items in a list.


# Get the input form the user
user_input = input("Enter the list of number to sum. \n").split()
user_input_integer = list(map(lambda x: int(x), user_input))

# program logic
sum_ = 0

for num in user_input_integer:
    sum_ += num

print(sum_)
