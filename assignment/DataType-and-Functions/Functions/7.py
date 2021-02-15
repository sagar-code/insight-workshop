# 7. Write a Python function to accepts a string and claculate the number of upper case letters and lower case letters.

# Sample String: 'The quick Brow Fox'
# Excepted Output:
# No. of Uppercase characters: 3
# No. of Lowercase characters: 12


# Get the input from the user
user_input = input("Enter the string. \n").strip()
print(user_input)


def calc_case(string_):
    upper_counter = 0
    lower_counter = 0
    for i in string_:
        if i.isupper():
            upper_counter += 1
        elif i.islower():
            lower_counter += 1
        else:
            continue

    return upper_counter, lower_counter


result = calc_case(user_input)

print(f"No. of uppercase character: {result[0]}")
print(f"No. of lowercase character: {result[1]}")