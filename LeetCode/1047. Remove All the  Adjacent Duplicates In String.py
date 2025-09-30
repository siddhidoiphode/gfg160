class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack=[]
        for i in s:
            if stack and stack[-1]==i :
                stack.pop()
            else:
                stack.append(i)

        return "".join(stack)










# Description
# Accepted
# Accepted
# Editorial
# Editorial
# Solutions
# Solutions
# Submissions
# Submissions


# Code
# Testcase
# Testcase
# Test Result
# 1047. Remove All Adjacent Duplicates In String
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

 

# Example 1:

# Input: s = "abbaca"
# Output: "ca"
# Explanation: 
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
# Example 2:

# Input: s = "azxxzy"
# Output: "ay"
