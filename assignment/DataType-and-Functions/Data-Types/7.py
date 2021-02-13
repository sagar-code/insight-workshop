# 7. Write a Python function that takes a list of words and returns the length of the longest one.

# Get the input from the user
user_input = input("Enter the list of the words. \n")


# function to find longest word
def max_word_length(user_input_as_parameter):
    user_input_list = user_input_as_parameter.split()
    result = max(user_input_list, key=len)
    return len(result)


final_result = max_word_length(user_input)
print(final_result)