# 1.1 Reverse an array in-place (without using extra space)
# Problem: Given an integer array, reverse it in-place without using another array.
# Example:
# Input: [1, 2, 3, 4] → Output: [4, 3, 2, 1]

arr=[]
arr = list(map(int , input("Enter elemets of arrary seprated by space: ").strip().split()))
left = 0
right = len(arr)-1

while left < right:
    arr[left] , arr[right] = arr[right] , arr[left]
    left +=1
    right -=1
print("Reversed array:", arr)

