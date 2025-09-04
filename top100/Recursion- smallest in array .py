
i=0
minor = float('+inf')

def smallest(arr):
    global minor , i
    if not arr:
        return -1
    if i >= len(arr):
        return minor
    if arr[i]<minor and i<len(arr):
        minor=arr[i]
    i+=1
    return smallest(arr)

arr=[1,2,3,4,56,7,7,767,66,2]
print(smallest(arr))

