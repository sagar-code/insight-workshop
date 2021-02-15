# 11. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also
# create a lambda function that multiplies argument x with argument y and print the result.


# Get the input from the user
a = int(input("Enter the number to add. \n"))
x, y = input("Enter two number to multiply. \n").split()

# lambda function
add_lambda = lambda a: a + 15
print(add_lambda(a))

mul_lambda = lambda x, y: int(x) * int(y)
print(mul_lambda(x, y))
