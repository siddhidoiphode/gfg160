n=int(input("Enter number of rows: "))
m=n
while n>0 :
    print(" "*(m-n) + "*"*n)
    n-=1

# This also works
# n = int(input("Enter number of rows: "))
# m=n
# for i in range(0,n):
#     print(" "*i + "*"*m)
#     m-=1

"""
******
 *****
  ****
   ***
    **
     *
"""

