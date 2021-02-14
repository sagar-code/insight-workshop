# 21. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given
# list of non-empty tuples.

# Sample List: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Excepted Result: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


# Sample list
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

result = sorted(sample_list, key=lambda item: item[1], reverse=False)
print(result)