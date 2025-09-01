import numpy as np

matrix=np.random.randint(1,16,size=(3,3))
print(matrix)
matrix=np.sort(matrix , axis=None).reshape(matrix.shape)
print(matrix)

