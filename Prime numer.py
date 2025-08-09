
prime =[]
m=50
for n in range(2,m+1):

    flag = 0
    for i in range(2,n//2):

        if n%i == 0:
            flag+=1
    if flag == 0:
        prime.append(n)
    





