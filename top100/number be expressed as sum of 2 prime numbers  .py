import sys

n=14
print("number : ",n)
c=0
li=[]
for i in range(2,n+1):
    f=0
    for j in range(2,(i//2)+1):
        if i%j == 0:
            f=1
            break
    if f==0:
        li.append(i)
print(li)

# for i in li:
#     if n-i in li:
#         print("Pair is ",i,n-i)
#         c=1
#         sys.exit(0)

low=0
high=len(li)-1
target=n
sum=0

while low<= high:
    sum=li[low]+li[high]
    if sum == target:
        print( li[low],li[high] )
        c=1
        break
    elif sum < target:
        low+=1
    else:
        high -= 1
        

if c==0:
    print("no")
