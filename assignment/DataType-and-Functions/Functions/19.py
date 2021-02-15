# 19. Write a Python program to create Fibonacci series uptop n using Lambda.


# import the reduce module
from functools import reduce

# Get the input from the user.
user_input = int(input("Enter the integer. \n"))

# logic
fib = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n-2), [0, 1])

print(fib(user_input))