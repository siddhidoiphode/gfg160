def insertionSort(arr):  

        for B in range(1,len(arr)):
          b=B
          while b>0 and arr[b]<arr[b-1] :
            #    ascending order

            # while b>0 and arr[b] > arr[b-1] :
            #    decending order
               
               arr[b] , arr[b-1] = arr[b-1] , arr[b]
               print(arr)
               b-=1

        print(arr)
        
arr=[23,43,4,5667,89,]
insertionSort(arr)
