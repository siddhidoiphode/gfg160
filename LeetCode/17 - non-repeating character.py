from collections import Counter
a=[1,2,32,34,8,56,3,89,789,56,341,5,678,43,7,8346,7,2,689,0]
c=dict(Counter(a))
print(c)
# print(i for i in c.values  if i==1)
nonReapeat = [num for num , freq in c.items() if freq==1]
print("ans",nonReapeat)








# from collections import Counter
# class Solution:
#     def nonRepeatingChar(self,s):
#         #code here
    
#         char_count = Counter(s)
        
#         for char in s:
#             if char_count[char] == 1 :
#                 return char
            
#         return '$'


# #{ 
#  # Driver Code Starts
# #Initial Template for Python 3

# import atexit
# import io
# import sys

# _INPUT_LINES = sys.stdin.read().splitlines()
# input = iter(_INPUT_LINES).__next__
# _OUTPUT_BUFFER = io.StringIO()
# sys.stdout = _OUTPUT_BUFFER


# @atexit.register
# def write():
#     sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


# if __name__ == '__main__':
#     t = int(input())
#     for i in range(t):
#         s = str(input())
#         obj = Solution()
#         ans = obj.nonRepeatingChar(s)
#         if (ans != '$'):
#             print(ans)
#         else:
#             print(-1)

#         print("~")

# # } Driver Code Ends