n=int(input("Enter the number of rows: "))

for i in range(1,n+1):
    # for j in range(1, n+1):

        if i==1 or i==n :
            print("* "* n)

        else :
            print("* " + "  "*(n-2)+ "*")

"""
* * * * * *
*         *
*         *
*         *
*         *
* * * * * *
"""