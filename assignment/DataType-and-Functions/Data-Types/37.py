# 37. Write a Python program to multiply all the items in a dictionary.

# Sample Dictionary:
dict_ = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# logic
result = 1

for value in dict_.values():
    result *= value

print(result)