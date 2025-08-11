



############################################# 1. Two Sum   ###############################################
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 



from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            if target - num in hash_map:
                return [hash_map[target - num], i]
            hash_map[num] = i
        return []
    
    

# 4. Why [hash_map[target - num], i]?
# hash_map[target - num] → index of the earlier number

# i → index of the current number (num)

# Together, [hash_map[target - num], i] is the pair of indices that make the sum.

# Example final step:

# vbnet
# Copy
# Edit
# nums = [2, 7, 11, 15]
# target = 9

# Step when num = 7 (i = 1):
#     target - num = 2
#     hash_map[2] → 0
# Return [0, 1]