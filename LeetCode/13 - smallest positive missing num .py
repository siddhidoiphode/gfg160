#User function Template for python3
class Solution:
    def missingNumber(self, arr):
        l = len(arr)

        # for i in range(n):
        #     if arr[i] <= 0 or arr[i] > n:
        #         arr[i] = n + 1

        # for i in range(n):
        #     num = abs(arr[i])
        #     if 1 <= num <= n:
        #         arr[num - 1] = -abs(arr[num - 1])

        # for i in range(n):
        #     if arr[i] > 0:
        #         return i + 1
        # return n + 1
      
        print(sorted(arr))
        for i in range(1,l+1) :
            
            if i not in arr:
                # print(i)
                return i
                
                break
            
            # 2 -3 4 1 1 7
            # 5 3 2 5 1 
            # -8 0 -1 -4 -3

import math


arr = [int(x) for x in input().strip().split()]
ob = Solution()
print(ob.missingNumber(arr))
     



