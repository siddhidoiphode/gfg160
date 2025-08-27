
# If n = 5
# 1*2*3*4*5*26*27*28*29*30
#   6*7*8*9*22*23*24*25
#     10*11*12*19*20*21
#       13*14*17*18
#         15*16

# If N = 2
# 1*2*5*6
#   3*4

# If N = 4
# 1*2*3*4*17*18*19*20
#   5*6*7*14*15*16
#     8*9*12*13
#       10*11

n=5
sum=n*(n+1)
print(sum)
start=1
end=sum-n+1
spaces=1
for i in range(n,0,-1):
    row='' 
    print(" "*spaces,end="")
    spaces+=1
    for j in range(i):
        row += str(start)+"*"
        start+=1
    for k in range(end,end+i):
        row+= str(k)+"*"

    print(row)
    end-=i-1
        