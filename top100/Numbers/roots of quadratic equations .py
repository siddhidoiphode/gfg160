import math
print("ax^2+bx+c=0\nAbove is the quadratic equation \nprovide values of a & b,c")
a,b,c=list(map(int,input().split()))
print(a,b)
print(f"Equation will be:  {a}x^2 + {b}x +{c} = 0")

d= (b*b) - (4*a*c)
x1= (-b - math.sqrt(d)) /(2*a) 
x2= (-b + math.sqrt(d)) /(2*a)
print(x1,x2)