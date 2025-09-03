
def isArmstrong(n):
    sum1=0
    l=len(str(n))
    sum1=sum(int(j)**l for j in str(n))
    return sum1==n

start = 100
end= 200

for i in range(start,end+1):
    if isArmstrong(i):
        print(i)


# ###### CORRECT
# start = 100
# end= 10000
# for i in range(start,end+1):
#     sum1=0
#     l=len(str(i))
#     sum1=sum(int(j)**l for j in str(i))
#     if sum1==i:
#         print(i)
    