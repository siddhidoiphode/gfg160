


def MaxSumArray(arr):

    Narr= arr[:len(arr)] 
    # + arr[:-1] 
    print(Narr)
    if not Narr :
        return 0
    else:

        maxSum = arr[0]
        minSum = arr[0]
        result = arr[0]

        for i  in range(1,len(Narr)):

            num=Narr[i]
            Tmax = max( num , num + maxSum , num + minSum )
            Tmin = min( num , num + maxSum , num + minSum )
                    
            maxSum = Tmax
            minSum = Tmin
            result= max(result , maxSum)
                    
        return result
    

# arr=list(map(int,input("").strip()))
arr = list(map(int, input().strip().split(",")))
ans=MaxSumArray(arr)
print(ans)

