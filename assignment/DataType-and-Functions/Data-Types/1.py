# 1. Write a Python program to count the number of characters (Character frequency) in a (string).

# Sample String: google.com
# Excepted Result: {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}


# Get the string from the user
user_string = input("Enter the string to count the number of character?\n")

# count the string
result = dict()

for char in user_string:
    if char in result.keys():
        result[char] += 1
    else:
        result[char] = 1

# sort the dictionary by the result
sorted_result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)}

print(sorted_result)

