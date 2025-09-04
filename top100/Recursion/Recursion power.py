
# # RECURSION POWER

# n=2
# p=3
count=0
def power(n,p):
    if p ==1:
        return n
    p-=1
    return n*power(n,p)
print(power(5,3))
