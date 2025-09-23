# Correct
# n = int(input(" "))
# s=''
# s+= "".join(map(str ,range(1,n+1)))
# space=0
# for i in range(1,n+1):


#     p=s[ 0 : n-i+1 ]
#     r= p[::-1]
#     r= r[1:]
#     print(" "*space + p + r," ",i)
#     space +=1
     

n=4
s="".join(map(str,range(1,n+1)))  #1234
print("s:",s)
col=(2*n)-1
for i in range(1,n+1):
    print(( s[:]+s[::-1][1:] ).center(col," "))
    s=s[:-1]
    # print(( s[:-i]+s[:-i][::-1][i+1:] ).center(col," "))
"""
1234321
 12321
  121
   1"""