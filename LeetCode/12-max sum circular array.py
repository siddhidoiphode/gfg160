
# def MaxSumCircularArray(arr):

#     Narr= arr[:len(arr)] + arr[:-1] 
#     print(Narr)
#     if not Narr :
#         return 0
#     else:

#         maxSum = arr[0]
#         minSum = arr[0]
#         result = arr[0]

#         for i  in range(1,len(Narr)):

#             num=Narr[i]
#             Tmax = max( num , num + maxSum , num + minSum )
#             Tmin = min( num , num + maxSum , num + minSum )
                    
#             maxSum = Tmax
#             minSum = Tmin
#             result= max(result , maxSum)
                    
#         return result
    

# # arr=list(map(int,input("").strip()))
# arr = list(map(int, input().strip().split(",")))
# ans=MaxSumCircularArray(arr)
# print(ans)
		 
# arr=[1,2,3,4,5,6,7,8,9,10]
# a= arr[:4]
# b= arr[:len(arr)]
# c= arr[2:]
# print(a , b, c)


# def MaxSumArray(arr):

#     print(arr)
#     if not arr :
#         return 0
#     else:
#         minSum = arr[0]
#         result = arr[0]

#         for i  in range(1,len(arr)):

#             num=arr[i]
#             minSum = min( num  , num + minSum )
#             result= min(result , minSum)
            
#         ans=sum(arr)-result

#         minisum=result
#         if minisum == sum(arr):
#             return max(arr)
#         else:
#             return ans
    
# arr = list(map(int, input().strip().split(" ")))
# ans=MaxSumArray(arr)
# print(ans)





def maxSubArray(arr):
    if not arr:
        return 0  # Handle empty array case

    max_sum = arr[0]  # Initialize with first element
    current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)  # Either extend the current subarray or start new
        max_sum = max(max_sum, current_sum)  # Update max_sum if current sum is larger

    return max_sum

# Input handling
arr = list(map(int, input().strip().split()))
print(maxSubArray(arr))




