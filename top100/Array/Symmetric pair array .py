
import numpy as np 
from collections import Counter
ans=[]
arr=np.array([(10, 20), (30, 40), (20, 10), (50, 60), (40, 30), (60, 50), (70, 80), (80, 70), (90, 100)])
# print(arr arr[2][::-1] in arr)
# ans=[arr[i] if arr[i][::-1] in arr]
for i in range(len(arr)):
    if arr[i][::-1] in arr:
        ans.append(arr[i])

print(ans)

