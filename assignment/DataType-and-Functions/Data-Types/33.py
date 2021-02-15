# 33. Write a Python script to print a dictionary where the keys are number between 1 to 15 (both included) and the
# values are the square of keys.

# Sample Dictionary:
# {1: 1, 2: 4, 3: 9, 4: 14, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}


# program logic
result = {i: i*i for i in range(1, 16)}
print(result)