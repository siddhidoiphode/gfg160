#            1
#            4*5*6
#            2*3
#            7*8*9*10

n=4
sum=0
rows=[]
for i in range(1,n+1):
    row=''
    for j in range(1,i+1):
        sum+=1
        row+=str(sum)+"*"

    rows.append(row[0:len(row)-1])

print(rows)

for i in range(len(rows)):
    if i%2 == 0:
        print(rows[i])

for i in range(len(rows)):
    if i%2 != 0:
        print(rows[i])
        