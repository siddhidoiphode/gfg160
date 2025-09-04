
# 3 sort elements by frequency
import numpy as np
from collections import Counter

li = [1, 23, 2, 3, 3, 23, 211, 1, 1, 2, 11, 2, 3, 32, 3, 22]
c = Counter(li).most_common()
# c= c.most_common()
print(c)
ans = [item for item,freq in c for _ in range(freq)]

print(ans)
# k=c.keys()
# v=c.values()

# print(k)
# print(v)
