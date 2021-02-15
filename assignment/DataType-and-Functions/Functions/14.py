# 14. Write a Python program to sort a list of dictionaries using Lambda.


# Sample Dictionary
dict_ = [
    {'a': 23, 'age': 24},
    {'b': 2, 'age': 23},
    {'c': 12, 'age': 12},
    {'d': 32, 'age': 27},
    {'e': 1, 'age': 29}
]

# sorting using lambda
sorted_dict = sorted(dict_, key=lambda x: x['age'], reverse=True)
print(sorted_dict)