# 9. Write a binary search function. It should take a sorted sequence and
# the item it is looking for. It should return the index of the item if found.
# It should return -1 if the item is not found.

def binary_search(arr, item):
    for i in range(len(arr)):
        if item in arr:
            return arr.index(item)
        else:
            return -1


arr_list = [1, 2, 4, 5, 6, 7, 9, 10]

n = int(input("Enter the integer to find: "))
print(binary_search(arr_list, n))