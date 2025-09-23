

# n=int(input(" "))
# m=n
# s=''
# for i in range(1,n+1):
#     if i==1:
#         s+=str(i)
#         print(" "* (m-i)  +  s   )
#     else:
#         s+=str(i)
#         print(" "*(m-i) + s[:-1]+ s[: : -1] )

n=5
s=''
col=(2*n)-1
for i in range(1,n+1):
    s+=str(i)
    print((s+s[::-1][1:]).center(col," "))


"""
    1    
   121   
  12321
 1234321
123454321
"""
