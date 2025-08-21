n = int(input(" "))
s=''
s+= "".join(map(str ,range(1,n+1)))
space=0
for i in range(1,n+1):
    # print("---", n , i)
    # if i==n:
    #     print(" "*space + "1" )
    p=s[ 0 : n-i+1 ]
    r= p[::-1]
    r= r[1:]
    print(" "*space + p + r," ",i)
    space +=1
     
