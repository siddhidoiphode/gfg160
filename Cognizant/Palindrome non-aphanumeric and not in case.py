
# 1.2 Check if a string is a palindrome (ignore case & non-alphanumeric)
# Problem: Given a string, check if it reads the same forwards and backwards, ignoring case and non-alphanumeric characters.
# Example:
# Input: "A man, a plan, a canal: Panama" → Output: True                                                                 (ignore case & non-alphanumeric)means?


import re

class Palindrome:

    def isPalindrome(self , s):

        cleaned = re.sub( r'[^a-zA-Z0-9]',"",s).lower()
        print("Cleaned string:", cleaned)
        rev = cleaned[::-1]

        if cleaned == rev:
            print("Palindrome")
        else:
            print("Not Palindrome")

s = input("Enter a string: ").strip()
obj = Palindrome()
obj.isPalindrome(s)


