# 9. Write a Python function that takes a number as a parameter and check the number is prime or not.

# Note: A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other that 1
# and itself.


# Get the input from the user
user_input = int(input("Enter the integer. \n"))


def check_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


result = check_prime(user_input)
print(result)
