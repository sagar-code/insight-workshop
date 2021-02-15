# 6. Write a Python function to check whether a number is in given range.


# Get the input from the user
user_input = int(input("Enter the non-negative integer. \n"))


def is_in_range(n):
    if n in range(1, 9):
        return "The given number is in the range."
    else:
        return "The given number is not in the range."


result = is_in_range(user_input)
print(result)