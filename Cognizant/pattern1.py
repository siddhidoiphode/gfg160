
        #    2
        #    4 3
        #    7 6 5
        #    11 01 9 8
        #    1110198
        #    765
        #    43
        #    2

n=4
start = 2

for i in range(1,n+1):
    row=''
    
    for j in range(i):
        row+=" "+ (str(start))
        
        start+=1
    print( row[::-1])


# n=4
# s=2
# rows1=[]
# for i in range(1,n+1):
#     rows=''
#     for j in range(s,s+i):
#         rows += str(j)
#     print(rows[::-1])
#     rows1.append(rows)
#     s=s+i

# for row in reversed(rows1):
#     print(row[::-1])

