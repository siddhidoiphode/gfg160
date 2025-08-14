from collections import Counter
s= "siddhi"
a={}
a=dict(Counter(s))
print(a)
m=max(a, key=a.get)
print(m)

