def insertionSort(arr,arr_len):
 for i in range(1,arr_len):
      key=arr[i]
      j=i-1
      while j>=0 and key<arr[j]:
        arr[j + 1] = arr[j]
        j = j - 1
      arr[j+1] = key

arr = [12, 1,6,78,25,33,35,65,100]
arr_len=len(arr)
insertionSort(arr,arr_len)
print(arr)      
