# 28. Write a Python script to add a key to a dictionary.

# Sample Dictionary: {0: 10, 1: 20}
# Excepted Result: {0: 10, 1: 20, 2: 30}


# Get the sample dictionary
sample = {0: 10, 1: 20}

# adding key to a dictionary
added_key = {2: 20}

# using update method
sample.update(added_key)
print(sample)

# directly adding key
sample[3] = 40

print(sample)