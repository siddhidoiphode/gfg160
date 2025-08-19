# Functions 

# map 
num = [1,2,3,4,5,6,7,8]
def add(a):
    return a+a

out = map(add , num )
add = list(out)
print("add : ",add)


multiply = map( lambda a:a*a , num)
print("multiply :",list(multiply))

# filter()

def add(a):
    if (a>5):
        return a

out_f = filter(add,num)
out_m = map(add,num)

print("filter ",list(out_f),"map",list(out_m))
# multiply : [1, 4, 9, 16, 25, 36, 49, 64]
# filter  [6, 7, 8] map [None, None, None, None, None, 6, 7, 8]

# reduce()
from functools import reduce
 
li_1 = reduce( lambda a,b:a+b , [10,20,30])
print(li_1)

def cus_add(f,s):
    return f+s

li2=[10,20,30]
li_2=reduce(cus_add , li2)
print(li_2)


# add :  [2, 4, 6, 8, 10, 12, 14, 16]
# 60
# add :  [2, 4, 6, 8, 10, 12, 14, 16]
# multiply : [1, 4, 9, 16, 25, 36, 49, 64]
# filter  [6, 7, 8] map [None, None, None, None, None, 6, 7, 8]
# 60
# 60
