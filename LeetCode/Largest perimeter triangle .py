class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort(reverse=True)
        max_sum = 0

        for i in range(len(nums)-2):
            a,b,c= nums[i], nums[i+1], nums[i+2]
            if a < b+c :
                if a+b+c > max_sum:
                    max_sum= a+b+c
                    print(a,b,c)

        return max_sum
    


        


############### CORRECT BUT TIME COMPLEXITY IS O(N^3)  ##################
# nums=[2,1,2]
# l=len(nums)
# max_sum = 0
# for i in range(l):
#     for j in range(i+1, l):
#         for k in range(j+1, l):
#             a, b, c = nums[i], nums[j], nums[k] 
                   
#             if a + b > c and b + c > a and a + c > b:
#                 if a + b + c > max_sum:
#                     max_sum = a + b + c
                
# print(max_sum)





# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

 

# Example 1:

# Input: nums = [2,1,2]
# Output: 5
# Explanation: You can form a triangle with three side lengths: 1, 2, and 2.
# Example 2:

# Input: nums = [1,2,1,10]
# Output: 0
# Explanation: 
# You cannot use the side lengths 1, 1, and 2 to form a triangle.
# You cannot use the side lengths 1, 1, and 10 to form a triangle.
# You cannot use the side lengths 1, 2, and 10 to form a triangle.
# As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.
 

# Constraints:

# 3 <= nums.length <= 104
# 1 <= nums[i] <= 106