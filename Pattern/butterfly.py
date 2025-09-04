
k=int(input("Enter the number of rows: "))
mid , cen , string ,cen2 = k//2 , k-2 ,"" , 2

for i in range(1, k + 1):
    if i <=mid+1:
        string=" "*cen
        print(string.center(k,"*"))
        cen=cen-2
    else:
        string=" "*cen2
        print(string.center(k,"*"))
        cen2+=2


"""
*        *
**      **
***    ***
****  ****
**********
**********
****  ****
***    ***
**      **
*        *
"""

         