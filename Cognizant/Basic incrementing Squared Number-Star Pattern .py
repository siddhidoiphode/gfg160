
        #    1*2*3*4
        #    5*6*7*8
        #    9*10*11*12
        #    13*14*15*16

value=4
num=1
for i in range(1,value+1):
    for j in range(value):
        print(f"{num}*",end='')
        num+=1
    print()

    