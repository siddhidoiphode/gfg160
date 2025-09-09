import numpy as np

import array
a=array.array('f',[1,3,4])
print(a)
arr=np.array([0,0,1,2,3,4,12,1,2,0],dtype='int')
last=float('+inf')
latest=float('+inf')

for i in set(arr):
    print("i",i)
    if  i<= last and i<latest:
        last =i
        print(i)
    if  i > last and i<latest :
        latest=i
        # last=latest


print("last",last)
print("latest",latest)


print("----------------- SUM OF ARRAY ------------------")

s1=np.sum(arr)
print("SUM ",s1)
