# Sort first half in ascend other in descending 

import numpy as np
import array

a=np.array([1,3,4,2,5,7,8,6,10,9])

a1=a[:len(a)//2]
a2=a[len(a)//2:]

print(a1)
print(a2)
# print(a2.tolist())

a1=np.sort(a1)
print("a1",a1)

a2=np.sort(a2)
a2=a2[::-1]
print("a2",a2)

