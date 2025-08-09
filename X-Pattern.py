
n=int(input("Enter the number of rows: "))

for i in range (1,n):

    if i <= n//2 +1 :
            
        if i==n//2 +1:
            print( "  "*(i-1)  +  "* "+  "  "*(n-(2*i)) +  "  "*(i-1)  ) 

        else:
            print( "  "*(i-1)  +  "* "+  "  "*(n-(2*i))  + "* " +  "  "*(i-1)  ) 

    else:

         print( "  "*(i-1)  +  "* "+  "  "*(n-(2*i))  + "* " +  "  "*(i-1)  ) 
    


    