


def LCM(a,b,lcm=None):
    if lcm==None:
        lcm=max(a,b)
  
    if lcm%a==0 and lcm%b==0:
        return lcm
    else:
        return LCM(a,b,lcm+1)

a,b = 7,3
print(f"Lcm of {a},{b} :",LCM(a,b))






# def lenString(s,i=0):
#     try:
#         # if not i:
#         #     i=0

#         if s[i]:
#             i+=1
#     except IndexError:
#         return i
#     return lenString(s)


# s='siddhu'
# print("Length of string is ",lenString(s))