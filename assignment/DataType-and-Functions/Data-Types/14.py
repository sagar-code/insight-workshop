# 14. Write a Python function to create the HTML string with tags around the word(s).

# Sample function and result:
# add_tags('i', 'Python') => '<i>Python</i>'
# add_tags('b', 'Python Tutorial') => '<b>Python Tutorial</b>'


# Get the input from the user
input_tag = input("Enter the tag of HTML. \n")
input_text = input("Enter the text to create a HTML string. \n")


# creating function
def add_tags(tag_name, text):
    return f"<{tag_name}> {text} </{tag_name}>"


result = add_tags(input_tag, input_text)
print(result)