        #    7*8*9*10
        #    4*5*6
        #    2*3
        #    1

n=4
sum = (n*(n+1))/2
print(sum)
start=int(sum)-n+1
for i in range(n,0,-1):
    
    row=''
    for j in range(start,start+i):
        row += str(j)
    print(row)
    start-= i-1





