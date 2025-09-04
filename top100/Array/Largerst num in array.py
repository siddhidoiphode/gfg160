import numpy as np 
# import array
# a=array.array('i',[10,20,30,40])
# print("array.aray",a)

print("------------------------------ Max in Array --------------------------------")
arr=np.array([1,2,3,45,7,4])
m=np.max(arr)
print("Max ele in arr : ",m)


print("------------------------------ Min in Array --------------------------------")
try:
    arr1=np.array([0,-1])
    m1=np.min(arr1)
    print("Min ele in arr : ",m1)
except ValueError:
    print("Array is empty")



