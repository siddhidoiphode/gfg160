
class C:
    def triplet(self,nums):
       
        ans = [nums[i] < nums[i+1] and nums[i+1] < nums[i+2]  for i in range (len(nums))  if i+2 < len(nums) ]
        print(ans)
     
        for i in ans:
            if i == True:
                return 'true'
       
        return 'false'
        
obj=C()
nums = [2,1,5,0,4,6]
result= obj.triplet(nums)
print(result)


# Increasing continue Triplet Subsequence
# Topics
# premium lock icon
# Companies
# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k are consecutives and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# Example 2:

# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
# Example 3:

# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 
