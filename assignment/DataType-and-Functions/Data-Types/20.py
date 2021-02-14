# 20. Write a Python program to count the number of strings where the string length is 2 or more and the first and last
# character are same from a given list of string.

# Sample List: ['abc', 'xyz', 'aba', '1221']
# Excepted Result: 2


# Get the input from the user
user_input = input("Enter the list of element. \n").split(',')

# program logic
counter = 0

for item in user_input:
    if (len(item) > 2) and (item[0] == item[-1]):
        counter += 1

print(counter)