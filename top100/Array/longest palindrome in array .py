
import numpy as np
ans=""
arr=np.array(['1','a','z','z','a','1','1','z'])
# arr = ['1','a','z','z','a','1','1','z']
for i in range(len(arr)):
    temp=''
    for j in range(i+1,len(arr)):
        # temp = arr[i:j+1]
        temp = "".join(map(str,arr[i:j+1]))
        print("t",temp,temp[::-1])
        rev= temp[::-1]
        print(temp == rev)
        print(temp[::-1])
        if (temp == rev) and (len(temp)>len(ans)):
            ans=temp
            print(ans)


print("ans",list(ans))

