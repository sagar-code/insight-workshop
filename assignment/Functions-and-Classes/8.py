# 8. Write a function, is_prime, that takes an integer and returns True if the
# number is prime and False if the number is not prime.


def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0 and num != i:
                return False
    return True


n = int(input("Enter a Number: "))
print(is_prime(n))