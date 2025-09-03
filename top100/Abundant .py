n=int(input("Enter number: "))
factors=[i for i in range(1,n) if n%i==0]
print(factors)
if (sum(factors)>n):
    print("Abundant number")
else:
    print("Not Abundant number")

