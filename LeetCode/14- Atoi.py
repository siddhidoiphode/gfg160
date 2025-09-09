
# #User function template for Python

# class Solution:
#     def myAtoi(self, s):
#         # Code here
#         count = 0
#         ans = 1
#         m = 1
#         final = 0
#         alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#         N = '0123456789'
        
#         if '-' in s :
#             ans = -1
            
#         for i in s:
#             if i.isdigit():
#                 count += 1
#             else:
#                 break
                
#         # print("c",count)
#         Nstr = s[:count]
        
#         # print(Nstr)

#         for i in range(len(Nstr)-1 , -1 ,-1):
#             if Nstr[i] in N :
#                 # print("NSTR[i]",Nstr[i])
#                 final += (int(Nstr[i]) * m)
#                 m *= 10
#             else:
#                 break
        
#         final *= ans
        
#         big = 2**(31) - 1
#         small = -2**(31)
        
#         if final > big :
#             return(big)
#         elif final< small :
#             return(small)
#         else :
#             return(final)
        





# if __name__ == '__main__':

#         s = input()
#         ob = Solution()
#         print(ob.myAtoi(s))
#         print("~")

# } Driver Code Ends



# s = input().strip()
# sign =1
# result=idx=0

# if idx < len(s) and (s[idx] == '-' or s[idx] == '+'):
#     if s[idx] == '-':
#         sign = -1
#     idx += 1


# while idx < len(s) and '0'<= s[idx] <= '9' :
#     result = result *10 + ( ord(s[idx])- ord('0'))
#     idx+=1

# result = result *sign

# if result > 2**(31) - 1 :
#         print( (2**(31)-1 ) )
# elif result < -  2**(31):
#         print(-(2**(31)) )
# else:
#         print(result)



#User function template for Python

class Solution:
    def myAtoi(self, s):
        # Code here
        s=s.strip()
        i=res=0
        sign=1 
        
        if i<len(s) and (s[i]=='+' or s[i]=='-'):
            if s[i] == '-':
                sign = -1
            i+=1
            
        while i < len(s) and '0'<=s[i]<='9' :
            res=res*10 + (ord(s[i]) - ord('0'))
            i+=1
            
        res*=sign
        
        if res > 2**(31) -1 :
            return 2**(31) -1
        elif res < -2**31 :
            return  -2**31 
        else:
            return res
        
        
    

#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")

# } Driver Code Ends