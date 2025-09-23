       
        #    13*14*15*16
        #    9*10*11*12
        #    5*6*7*8
        #    1*2*3*4


n=int(input("Enter number:"))
square=n**2
start = square-n+1 #16-4= 12

for i in range(n):
    rows=''
    for j in range(n):
        rows += str(start)+"*" 
        start+=1
    print(rows[:len(rows)-1])
    start= start-(2*n)


        #    7*8*9*10
        #    4*5*6
        #    2*3
        #    1

n = 4
total= ( n*(n+1) )//2
start = total-n+1

for i in range(n,0,-1):
    row=''
    for j in range(i):
        row+= str(start)+"*"
        start+=1
    print(row[:len(row)-1])
    start= start - (2*i) + 1
    # print(start,"=")

