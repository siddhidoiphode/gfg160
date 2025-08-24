        #    1112131415      
        #    10987 
        #    456 
        #    32 
        #    1 


n=int(input("Enter number: "))
total= n * (n+1)//2
start = total - n + 1
# print(start)

for i in range(n,0,-1):
    row=''
    for j in range(start,start+i):
        row += str(j)
    print(row)
    start -= i - 1
    
