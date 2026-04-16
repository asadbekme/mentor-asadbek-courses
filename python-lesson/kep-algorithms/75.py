def is_palindrome(s):
    return s == s[::-1]

s = input().strip().lower()
print(is_palindrome(s))