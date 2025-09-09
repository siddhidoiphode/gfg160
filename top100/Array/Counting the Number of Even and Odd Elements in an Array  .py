
import numpy as np
from collections import Counter
import array
li =np.array( [1, 23, 2, 3, 3, 23, 211, 1, 1, 2, 11, 2, 3, 32, 3, 22])
even=0
odd =0
for i in li:
    if i%2 ==0:
        even+=1
    else:
        odd+=1

print(even,odd)