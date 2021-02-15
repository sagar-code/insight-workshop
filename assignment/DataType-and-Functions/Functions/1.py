# 1. Write a Python function to find the Max of three numbers.

# Get the input from the user
n1, n2, n3 = input("Enter the three number to calculate the maximum number. \n").split()


# function to find the maximum number
def maximum_finder(a, b, c):
    if (a > b) and (a > c):
        maximum = a
    elif (b > a) and (b > c):
        maximum = b
    else:
        maximum = c

    return maximum


# call the function
result = maximum_finder(n1, n2, n3)
print(result)