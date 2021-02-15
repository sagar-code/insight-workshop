# 5. Write a  Python function to calculate the factorial of a number (a non negative integer). The function accepts
# the number as an argument.


# Get the input from the user
user_input = int(input("Enter the non-negative integer. \n"))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


result = factorial(user_input)
print(result)