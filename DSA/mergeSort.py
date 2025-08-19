

def merge(left,right,arr):
    i=j=k=0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            arr[k]=left[i]
            i+=1
            
        else:
            arr[k]=right[j]
            j+=1
        k+=1
        print(arr)

    print("1: ",arr)
    while i<len(left):
         arr[k]=left[i]
         i+=1
         k+=1

       
    print("2: ",arr) 
    while j < len(right):
         arr[k]=right[j]
         j+=1
         k+=1


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left= arr[:mid]
        right=arr[mid:]
        print('l:')
        mergeSort(left)
        mergeSort(right)
        merge(left,right,arr)
    
    print("0: ",arr,left,right)

arr = [2,4,1,41,74]
mergeSort(arr)
print(arr)
