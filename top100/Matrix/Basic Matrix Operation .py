import numpy as np

matrix=np.random.randint(1,16,size=(3,3))
print(matrix)
print()
matrix=np.sort(matrix , axis=None).reshape(matrix.shape)
print(matrix)
print("---------------------------")

#sort column wise
matrix1=np.random.randint(1,16,size=(3,3))
print(matrix1)
print()
matrix1 = np.sort(matrix1 , axis=0)
print(matrix1)
print()
print("---------------------------")

#sort row wise
matrix2=np.random.randint(1,16,size=(3,3))
print(matrix2)
print()
matrix2= np.sort(matrix2 , axis=1)
print(matrix2)
print()
 

print("-------------Reshape a 1D array of numbers 1-12 into a 3x4 matrix.--------------")
print()
# Reshape a 1D array of numbers 1–12 into a 3×4 matrix.
a=np.array(list(range(1,13)))
a=np.reshape(a,(3,4))
print(a)
print()


# Find the shape, size, and dimensions of a given matrix.
print("-------------Find the shape, size, and dimensions of a given matrix.--------------")
print()
m1=np.random.randint(1,10,size=(3,4))
print(m1)
print()
# m,n=len(m1),len(m1[0])
# print(f"Size = {m} X {n}")
# if m==n:
#     print("\nShape = Square")
# else:
#     print("\nShape = Rectangle")

print()
print("Shape: ",m1.shape)
print("Size: ",m1.size)
print("Dimention: ",m1.ndim)
print()

# Extract the 2nd row and 3rd column from a matrix.
print("-------------Extract the 2nd row and 3rd column from a matrix.--------------")
print()
m2=np.random.randint(1,10,size=(4,4))
print("\n",m2)
print()
print("2nd row" , m2[1])
print()
# print("3rd col" , m2[1])
# Extract 3rd column (index 2)
print("3rd column:", m2[:, 2])
print()


# Slice the top-left 2×2 submatrix from a 4×4 matrix.
print("---------Slice the top-left 2×2 submatrix from a 4×4 matrix..--------------")
print()
m3=np.random.randint(1,10,size=(4,4))
print(m3)
print("left 2x2\n", m3[:2, :2])



