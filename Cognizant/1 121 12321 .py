

n=int(input(" "))
m=n
s=''
for i in range(1,n+1):
    if i==1:
        s+=str(i)
        print(" "* (m-i)  +  s   )
    else:
        s+=str(i)
        print(" "*(m-i) + s[:-1]+ s[: : -1] )





