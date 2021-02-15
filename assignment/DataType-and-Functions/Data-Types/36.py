# 36. Write a Python program to sum all the items in a dictionary.

# Sample Dictionary:
dict_ = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

sum_ = 0
for v in dict_.values():
    sum_ += v

print(sum_)


# or
print(sum(dict_.values()))