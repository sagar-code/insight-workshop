# 12. Create a function, is_palindrome, to determine if a supplied word is
# the same if the letters are reversed.


def is_palindrome(string):
    new_string = string.replace(" ", "")
    if new_string.lower() == new_string[::-1].lower():
        return string + " is palindrome"
    else:
        return string + " is not palindrome"


n = input("Enter a word: ")
print(is_palindrome(n))