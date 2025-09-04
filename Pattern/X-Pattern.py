
n=int(input("Enter the number of odd rows: "))
center =1
for i in range (1,n+1):

    if i <= n//2 +1 :
            
        if i==n//2 +1:
            print( "  "*(i-1)  +  "* "+  "  "*(n-(2*i)) +  "  "*(i-1)  ) 
            val=i-1
        else:
            print( "  "*(i-1)  +  "* "+  "  "*(n-(2*i))  + "* " +  "  "*(i-1)  ) 
    else:
        print( "  "*(val-1)  +  "* "+  "  "*((2*center) - 1)  + "* " +  "  "*(val-1)  ) 
        val=val-1
        center+=1


"""
*           *
  *       *
    *   *
      *
    *   *
  *       *
*           *
"""