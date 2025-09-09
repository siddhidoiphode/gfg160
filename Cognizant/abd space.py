

s='  abc    efg  hij   hj '
ans=""
temp=''

for i in s:
    if i != " ":
        temp+=i
    else:
        ans+= temp[::-1]+' '
        temp=""

print(f'" {ans} "')

# s='  abc efg  hij '

# ans= s.split(" ")
# c=0
# for i in s:
#     if i == " ":
#         c+=1
#     else:
#         break
# print(" "*c,end=" ")

# for i in range(len(ans)):

#     if len(ans[i])!=0:
#         r=ans[i][::-1]
#         print(r ,end=" ")



s='  abc    efg  hij   hj '
ans=""
temp=''
for i in s:
    if i==" ":
        ans+=temp[::-1]+i
        temp=''
    else:
        temp+=i

print(ans)
