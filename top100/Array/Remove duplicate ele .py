import numpy as np
from collections import Counter
import array

li =np.array( [1, 23, 2, 3, 3, 23, 211, 1, 1, 2, 11, 2, 3, 32, 3, 22])
# s=[int(i) for i in set(li)]
# print(s)

c=Counter(li)
c_normal = {int(k): v for k, v in c.items()}
print(c_normal)

# ans={del c_normal[k] for k,v in c_normal.items() if v==1}
# print(ans)
for k in list(c_normal.keys()):
    if c_normal[k]> 1:
        del c_normal[k]

print(list(c_normal.keys()))
