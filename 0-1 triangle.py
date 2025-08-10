
n=int(input("Enter the number of rows: "))
s=""
for i in range(1,n+1):
        
        if i%2==1:   
           s="1 "+s     
           print(s)
           
        else:
            s="0 "+s
            print(s)

"""
1 
0 1
1 0 1
0 1 0 1
1 0 1 0 1
0 1 0 1 0 1
1 0 1 0 1 0 1

"""

