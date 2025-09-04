
import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9,10])
print(arr)
l=0
r=len(arr)-1

while l<=r :
    arr[l],arr[r] = arr[r],arr[l]
    l+=1
    r-=1
print("reversed array: ",arr)

