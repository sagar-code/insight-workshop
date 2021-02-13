# 11. Write a Python program to count the occurrences of each word in a given sentence.


# Get the input from the user
user_input = input("Enter the sentence. \n")

# program logic
word_list = user_input.split()
result = dict()

for word in word_list:
    if word in result.keys():
        result[word] += 1
    else:
        result[word] = 1

print(result)