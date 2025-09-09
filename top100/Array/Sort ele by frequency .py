
# 3 sort elements by frequency
import numpy as np
from collections import Counter
import array
li =np.array( [1, 23, 2, 3, 3, 23, 211, 1, 1, 2, 11, 2, 3, 32, 3, 22])
li1 =array.array('i', [1, 23, 2, 3, 3, 23, 211, 1, 1, 2, 11, 2, 3, 32, 3, 22])  #also works here

# res=[i for i in li if li.conj(i)==1]
c = Counter(li)
res=[int(i) for i,cnt in c.items() if cnt==1]
print(res)
# print(c)
# ans = [item for item,freq in c for _ in range(freq)]

# print(ans)
# k=c.keys()
# v=c.values()

# print(k)
# print(v)
