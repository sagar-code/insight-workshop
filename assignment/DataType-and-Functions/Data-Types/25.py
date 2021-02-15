# 25. Write a Python program to check whether all dictionaries in a list are empty or not.

# Sample List: [{}, {}, {}]
# Return Value: True

# Sample List: [{1, 2}, {}, {}]
# Return Value: False


# Get the sample list
sample_1 = [{}, {}, {}]
sample_2 = [{1, 2}, {}, {}]


# program logic
def check_empty(sample):
    return all(not item for item in sample)


print(check_empty(sample_1))
print(check_empty(sample_2))