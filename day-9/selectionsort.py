def selectionSort(arr,arr_len):
 for i in range(1,arr_len-1):
  min = i

  for j in range(i+1,arr_len):
      if arr[j]<arr[min]:
       min = j
      elif min!=i:
       arr[min], arr[i] = arr[i], arr[min]

arr = [12,44,18,23,65,75,89,101]
arr_len=len(arr)
selectionSort(arr,arr_len)
print(arr)
       
