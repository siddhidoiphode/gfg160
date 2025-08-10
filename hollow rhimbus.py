n=int(input("Enter the number of rows: "))

for i in range(1,n+1):
    left= n-i
    if i==1 or i==n:      
        print("  "*left + "* " *n)
    else:
        print("  "*left + "* " + "  "*(n-2)  + "*")




"""
               * * * * * * * * 
            *             *
          *             *
        *             *
      *             *
    *             *
  *             *
* * * * * * * *

"""