
n= 7
s="".join(map(str,range(1,n+1)))
# print(s)
print()


for i in range(0,n+1):
    pre = s[:(n-i)]
    suff = pre[:-1][::-1]
    print(" "*i + pre + suff)

"""
12321
 121
  1

"""
a=7
b="".join(map(str,range(1,a+1)))
# print(b)
for j in range(1,a+1):
    start = b[:j]
    end=start[:-1][::-1]
    print(" "*(a-j) + start +end)

"""
      1
     121
    12321
   1234321
  123454321
 12345654321
1234567654321

"""
print()
