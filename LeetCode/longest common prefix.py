# Input example: ["flower","flow","flight"]
# l = list(map(str.strip, input().strip("[]").replace('"','').split(",")))



from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # strs=list(map(str , input().strip("[]").replace('"',"").split(",")  ))

        if not strs:
            return ""
        
        m = min(strs , key=len)
        common=""
        for i in range(len(m)):
            char = m[i]
           
            if all(char==word[i] for word in strs):
                common +=char
            else:
                break
        return common
        





# 14. Longest Common Prefix
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.
