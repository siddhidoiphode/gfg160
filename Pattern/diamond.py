

a=int(input("Enter the number of odd rows: "))
mid=a//2

for i in range(1, a + 1):
    if i <= mid+1:
        left=mid-i+1
        cen=2*i -1 
        print("  "*left + "* "*cen )
    else:
        left= i-mid-1
        cen-=2
        print("  "*left + "* "*cen )



"""
        * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
"""