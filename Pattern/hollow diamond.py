i=int(input("Enter the number of odd rows: "))
mid=i//2

for a in range(1,i+1):

    if a <=mid+1 :
        left = mid-a+1
        cen=2*a-3
        if a==1 :
            print(f" "*left + "*")
        else:
            print(" "*left + "*" + " " *cen  + "*")

    else:
        left =a-mid-1
        cen=cen-2
        if a==i:
            print(" "*left + "*")
        else:
            print(" "*left + "*" + " " *cen  + "*")


"""
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
    
"""