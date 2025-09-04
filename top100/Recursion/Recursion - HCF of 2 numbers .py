hcf=1
i=1
def Hcf(a,b):
    global i,hcf
    m = min(a,b)
    if i>m:
        return hcf
    if a%i==0 and b%i==0:
        hcf = i
    i+=1
    return Hcf(a,b)

a,b = 15,45
print(Hcf(a,b))

