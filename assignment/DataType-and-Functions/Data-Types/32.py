# 32. Write a Python script to generate and print a dictionary that contains number (between 1 and n) in the form
# (x, x*x)

# Sample Dictionary: (n=5)
# Excepted Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# Get the input from the user
user_input = int(input("Enter the number. \n"))

result = {x: x*x for x in range(1, user_input+1)}
print(result)