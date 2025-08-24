
            # 2
            # 34
            # 567
            # 891011
            # 891011
            # 567
            # 34
            # 2 


n=4
total=( n*(n+1)//2 ) - 1
start=1
rows=[]
for i in range(1,n+1):
    p=''
    for j in range(i):
        start+=1
        p=p+str(start)
        print(start,end="")
    rows.append(p)
    print()


for row in reversed(rows):
    print(row)

