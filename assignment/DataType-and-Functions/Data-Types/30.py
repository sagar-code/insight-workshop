# 30. Write a Python script to check whether a given key already exists in a dictionary.


# Get the input form the user
user_input = int(input("Enter the key in integer. \n"))

# sample dictionary
dict_ = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}


# program logic
def check_duplicate_key(key):
    if key in dict_:
        return "Key is already exists in a dictionary."
    else:
        return "Key is not exist in a dictionary."


result = check_duplicate_key(user_input)
print(result)