import numpy as np

# Create a 3×3 zero matrix using NumPy.
matrix = np.zeros((3,3))
print(matrix)
print()
# Create a 4×4 identity matrix.
matrix1=np.ones((4,4))
print(matrix1)
print()
# Generate a random 5×5 matrix with integers between 1 and 50.
matrix2=np.random.randint(1,51,size=(5,4))
print(matrix2)
print()
# Create a diagonal matrix with values [1, 2, 3, 4].
matrix3 = np.zeros((4,4),dtype=int)
for i in range(4):
    matrix3[i][i]= int(i)+1

print(matrix3)
print()
# diagonal matrix directly
matrix4 = np.diag([1,2,3,4])   # diagonal matrix directly
print(matrix4)


