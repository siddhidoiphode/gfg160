import numpy as np

m1 = np.random.randint(1,20,size=(3,3))
m2 = np.random.randint(1,20,size=(3,3))

print(m1)
print()
print(m2)
print()
print("add \n" , np.add(m1,m2))
print()
print("substract \n" , np.subtract(m1,m2))
print()
print("multiply \n" , np.multiply(m1,m2))
print()
print("divide \n" , np.divide(m1,m2))
print()
print("floor_divide \n" , np.floor_divide(m1,m2))

