# 12. Write a Python script that takes input from the user and displays that input back in upper and lower cases.


# Get the input from the user
user_input = input("Enter the sentence. \n")

# program logic
upper_case_result = user_input.upper()
lower_case_result = user_input.lower()

print(upper_case_result, lower_case_result, sep='\n')