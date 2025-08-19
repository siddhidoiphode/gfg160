def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1] :
                # ascending order
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

arr=[12,6,28,12,4,2,2,1,4]
b=bubbleSort(arr)
print(b)

#---------------------------------------------------

def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1] :
                # Decending order
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

arr=[12,6,28,12,4,2,2,1,4]
b=bubbleSort(arr)
print(b)
