class Solution:
    def addDigits(self, num: int) -> int:

        while len(str(num)) > 1:
            sum1=0
            sum1=sum(map(int, str(num)))
            num=sum1
        print(num)


obj=Solution()
obj.addDigits(168115)







# num=38
# # n="".join(str(num))
# # print(n)
# sum=0
# while True:

#     for i in str(num):
#         sum+=int(i)
        
#     print("1",sum)
#     num=sum
#     print(len(str(num)))
#     if len(str(num))==1:
#         break

# print(num)




# Code
# Testcase
# Test Result
# Test Result
# 258. Add Digits
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

# Example 1:

# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.
# Example 2:

# Input: num = 0
# Output: 0
 