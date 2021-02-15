# Write a Python program to find if a given string starts with a given character using lambda.


# Get the input from the user
char_ = input("Enter the starting character. \n")
string_ = input("Enter the string. \n")

result = lambda x: True if x.startswith(char_) else False
print(result(string_))

