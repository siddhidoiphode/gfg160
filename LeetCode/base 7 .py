class Solution:
    def convertToBase7(self, num: int) -> str:
        ans=""
        if num == 0:
            return "0"
        Negative = num <0
        num=abs(num)

        while num > 0:
            reminder = num % 7 
            ans+= str(reminder)
            num //= 7
        ans = ans[::-1]

        return "-"+ ans if Negative else ans


# Code
# Testcase
# Test Result
# Test Result
# 504. Base 7
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer num, return a string of its base 7 representation.

 

# Example 1:

# Input: num = 100
# Output: "202"
# Example 2:

# Input: num = -7
# Output: "-10"
 