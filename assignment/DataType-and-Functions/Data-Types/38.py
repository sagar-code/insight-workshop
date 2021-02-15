# 38. Write a Python program to remove a key from a dictionary.

# Sample Dictionary:
dict_ = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

if 'c' in dict_.keys():
    del dict_['c']

print(dict_)