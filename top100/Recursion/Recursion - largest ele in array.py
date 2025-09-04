

i=0
major = float('-inf')

def largest(arr):
    global major , i
    if not arr:
        return -1
    if i >= len(arr):
        return major
    if arr[i]>major and i<len(arr):
        major=arr[i]
    i+=1
    return largest(arr)

arr=[]
print(largest(arr))
