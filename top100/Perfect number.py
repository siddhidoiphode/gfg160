

print("-------Perfect Numer-----------")
# n = int(input("Enter number: "))
n=28
factors=[ i for i in range(1,n) if n%i==0]
print(factors)
print( "Perfect Numer" if n==sum(factors) else "Not Perfect Number")



print("---------------------------")

import math

n=36
s=math.sqrt(n)
print(n,s==int(s))

