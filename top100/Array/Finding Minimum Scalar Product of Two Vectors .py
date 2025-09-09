# → Given two arrays (vectors), calculate the smallest possible sum of products of their corresponding elements.

import numpy as np
from collections import Counter
import array
li =np.array( [1, 23, 2, 3, 3, 23, 211, 1, 1, 2, 11, 2, 3, 32, 3, 22])
li1 =np.array( [11, 3, 32, 37, 78, 23, 11, 17, 71, 23, 111, 21, 32, 62, 3, 99])
m = float('+inf')

for i in range(len(li)):
    mul=li[i]*li1[i]
    if mul < m:
        m=mul
        
print(" ans: ",m)