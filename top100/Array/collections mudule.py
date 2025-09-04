
from collections import Counter
# DICTIONARY
print("______________________________ Dictionary ________________________________________________")
li=[1,23,2,3,3,23,211,1,1,2,11,2,3,32,3,22]
lis=Counter(li)
print(lis.pop(22))
print(lis.items())
print(lis.keys())
print(lis.values())
print(lis.get(32))
print(lis.most_common(2))
print(lis.popitem())
print(lis)

#DEQUE
print("____________________________________ Deque _____________________________________________")
from collections import deque

d=deque([1,23,4,56,78,23])
# d=[1,23,4,56,78,23] wrong way to do deque
print(d)

d.append(50)
print(d)
d.appendleft(60)
print(d)

d.pop()
print(d)
d.popleft()
print(d)

for i in d:
    print(i)

from collections import ChainMap
print("____________________________________ ChainMap _____________________________________________")

A={'a':1 , 'b':2 , 'c':3}
B={'a1':1 , 'b1':2 , 'c1':3}
C={'a2':1 , 'b2':2 , 'c2':3}
NEW={'z':10}
d=ChainMap(A,B,C)
print(d)
d=d.new_child(NEW)
print(d)