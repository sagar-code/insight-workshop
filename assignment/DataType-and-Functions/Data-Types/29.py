# 29. Write a Python script to concatenate following dictionary to create a new one.

# Sample Dictionary:
# dict1 = {1: 10, 2: 20}
# dict2 = {3: 30, 4: 40}
# dict3 = {5: 50, 6: 60}

# Excepted Result: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


# Get the sample dictionary
dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

# concatenating using kwargs
dict_ = {**dict1, **dict2, **dict3}
print(dict_)

# concatenating using loop
dict4 = {}
for d in (dict1, dict2, dict3):
    dict4.update(d)

print(dict4)
