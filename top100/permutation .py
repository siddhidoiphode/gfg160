
# permutation in which  n people can occupy r seat in class
import math


from itertools import permutations
print(math.perm(4,2))

people=[1,2,3,4]
perm = permutations(people,3)
perm = [i for i in perm]
print(perm)

