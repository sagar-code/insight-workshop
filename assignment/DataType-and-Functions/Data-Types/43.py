# 43. Write a Python program to remove an item from a tuple.

# Sample Tuples:
tuples = ('a', 'b', 3, 'c')

# remove a tuple from a list
result = tuple([i for i in tuples if type(i) == str])
print(result)