#User function Template for python3

# CORRECT
class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
   
    def Reverse(self,arr,start,end):
        while start< end :
            arr[start],arr[end] = arr[end] ,arr[start]
            start+=1
            end-=1
            
    def rotateArr(self, arr, d):
        #Your code here
        n = len(arr)
        d%=n
        
        self.Reverse(arr,0,d-1)
        self.Reverse(arr,d,n-1)
        self.Reverse(arr,0,n-1)
        

arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
d = 3

ans=[]
ans.extend(arr[d:])
ans.extend(arr[:d])
print(ans)
