

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
