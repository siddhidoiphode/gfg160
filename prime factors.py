n=int(input("Enter a number: " ))
m=n
flag=0
prime=[]
factors=[]
for j in range(2,n+1):
    flag=0
    for i in range(2, j//2 + 1):
        if j%i == 0:
          flag+=1
    if flag ==0:
       prime.append(j)

while n!=1 :
    for i in prime:
        if n%i==0:
            n=n//i
            factors.append(i)
        
print(prime)

print(factors)
if len(factors)==0:
    print(f"1 , {m}")

