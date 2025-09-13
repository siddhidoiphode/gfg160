
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0:
            return True
        size=len(flowerbed)
        for i in range(size):
            if flowerbed[i]==0:
                left = (i==0 or flowerbed[i-1]==0)
                right = (i==size-1 or flowerbed[i+1]==0)
            
                if right and left :
                    flowerbed[i]=1
                    n-=1
                    if n==0:
                        return True

        return n==0



# CORRECT 
#  class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         count=0
#         for i in range(len(flowerbed)):
#             # print('index',i)
#             # print(flowerbed[i])
#             if n==0:
#                 return True

#             if len(flowerbed)==1:
#                 if flowerbed[0]==0 and n==1:
#                     return True
#                 return False

#             if i==0:
#                 if flowerbed[i]==0 and flowerbed[i+1]==0 :
#                     flowerbed[i]= 1
#                     count+=1

#             elif i==len(flowerbed)-1:
#                 if flowerbed[i-1]==0 and flowerbed[i]==0 :
#                        flowerbed[i]= 1
#                        count+=1

#             else:
#                 # print("i",flowerbed[i])
#                 if flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0 :
#                     flowerbed[i]= 1
#                     count+=1
#             # print(i,' = ', flowerbed)
#         # print(count)
#         return count >= n













# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
