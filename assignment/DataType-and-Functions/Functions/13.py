# 13. Write a Python program to sort a list of tuples using lambda.


# Sample List of Tuples
list_of_tuples = [('a', 1), ('b', 10), ('c', 3), ('d', 2), ('e', 23)]

# sorting using lambda
list_of_tuples.sort(key=lambda x: x[1])

print(list_of_tuples)