# 4. Write a Python program to reverse a string.

# Sample String: "1234abcd"
# Excepted Output: "dcba4321"


# Get the input from the user
user_input = input("Enter the string. \n")


def reverse_string(string_):
    re_string = ""
    len_str = len(string_)

    while len_str > 0:
        re_string += string_[len_str - 1]
        len_str -= 1

    return re_string


result = reverse_string(user_input)
print(result)
