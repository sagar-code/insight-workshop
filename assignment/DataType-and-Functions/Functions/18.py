# 18. Write a Python program to check whether a given string is number or not using Lambda.


# Get the input form the user
user_input = input("Enter the number. \n")

lambda_number = lambda n: n.replace('.', '', 1).isdigit()

print(lambda_number(user_input))