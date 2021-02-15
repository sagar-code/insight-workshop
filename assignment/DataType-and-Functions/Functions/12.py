# 12. Write a Python program to create a function that takes one argument, and that argument will be multiplied with
# an unknown given number.


def random_number(n):
    return lambda i: i * n


result = random_number(2)
print(result(100))