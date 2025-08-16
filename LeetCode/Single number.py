class Solution:
    def singleNumber(self, nums ) :
        
        for i in nums:
            c = nums.count(i)
            if c == 1:
                return i
        
            
sol = Solution()
nums=[1,2,3,45,6,4,1,45,2,3,6]
Ans = sol.singleNumber(nums)
print("--> ",Ans)





# 136. Single Number
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]

# Output: 1

# Example 2:

# Input: nums = [4,1,2,1,2]

# Output: 4

# Example 3:

# Input: nums = [1]

# Output: 1