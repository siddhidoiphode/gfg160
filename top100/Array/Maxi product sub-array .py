import numpy as np
arr=np.array([2, 3, -2, 4, -1, 0, 1, -3, 2, -5, 4])
max_p = min_p = result =arr[0]

for num in arr[1:]:
    if num < 0:
        max_p , min_p = min_p , max_p

    max_p = max(num , num*max_p)
    min_p = min(num , num*min_p)

    result = max(result , max_p)

print(result)

