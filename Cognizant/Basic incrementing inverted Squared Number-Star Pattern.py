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
        print(f"{start}*",end="")
        start+=1
    print()
    start= start-(2*n)


