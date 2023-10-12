def is_palindrome(s: str) -> bool:
    return s == s[::-1]

input_string = ("pop")
if is_palindrome(input_string):
    print(f"{input_string} is a palindrome.")
else:
    print(f"{input_string} is not a palindrome.")
