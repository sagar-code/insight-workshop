# 15. Write a Python function to insert a string in the middle of a string.

# Sample function and result:
# insert_string_middle('[[]]', 'Python') => [[Python]]
# insert_string_middle('{{}}', 'PHP') => {{PHP}}


# Get the input from the user
string_input = input("Enter the symbol string. \n")
text_input = input("Enter the text. \n")


# function
def insert_string_middle(symbol, text):
    return f"{symbol[:2]}{text}{symbol[2:]}"


result = insert_string_middle(string_input, text_input)
print(result)