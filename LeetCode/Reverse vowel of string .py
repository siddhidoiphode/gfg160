class Solution: 
    def reverseVowels(self, s: str) -> str :
        if len(s)==0:
            return ""
        # v = ['a','e','i','o','u','A','E','I','O','U']
        v=set('aeiouAEIOU')   # use set for faster lookup
        current_vowels = [i for i in s if i in v]
        ans=''
        # last=-1
        # for i in s:
        #     if i in v :
        #         current_vowels.append(i)
        # print(current_vowels)

        for i in s:
            if i not in v:
                ans+= i
            else:
                ans+= current_vowels.pop()
        return ans



      
























# 345. Reverse Vowels of a String
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"