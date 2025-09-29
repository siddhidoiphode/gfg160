from typing import List

class Solution:
    def secondMax(self, nums: List[int]) -> int:
        f = s = float('-inf')
        
        for i in nums:
            if i in (f, s):  # skip duplicates
                continue
            
            if i > f:
                f, s = i, f
            elif i > s:
                s = i
        
        # if second max doesn’t exist, return max
        return s if s != float('-inf') else f


# Example usage:
data = [200, 500, 300, 250, 100, 300, 1100, 545, 650, 450, 250, 7000, 350]
sol = Solution()
print(sol.secondMax(data))  # Output: 1100
