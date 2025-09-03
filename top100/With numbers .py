# HCF highest common factor
import math
n=14
m=24

print("gcd of ",m,n,math.gcd(n,m))

# lcm lowest commom multiple

a=12
b=20

# print("lcm of ",a,b,math.lcm(a,b))

max_num =max(a,b)

while True:
    if max_num % a == 0 and max_num % b ==0 :
       print(a,b,"lcm :",max_num)
       break
    max_num +=1
    
