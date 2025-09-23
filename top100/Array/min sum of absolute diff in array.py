
import numpy as np
li =np.array([32, 1, 2, 3, 11, 211, 22, 23])
li.sort()
# print(list(int(i) for i in set(li)))
print(li)
median = li[len(li)//2]
print(sum(abs(median-num) for num in li))

