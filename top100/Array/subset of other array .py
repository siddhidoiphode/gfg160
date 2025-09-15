import numpy as np

A = np.array([12, 3])
B = np.array([3, 4, 5,12])

print(set(A).issubset((B)))

# if all ele are equal
print(len(set(A))==1)
