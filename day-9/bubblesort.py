def bubblesort(arr,arr_len):
 for i in range(0,arr_len-1):
  for j in range(0,arr_len-1):
    if arr[j]>arr[j+1]:
     arr[j], arr[j+1] = arr[j+1], arr[j]
     
arr = [14,27,33,35,10]
print("sorted Array : ",end='')


arr_len = len(arr)
bubblesort(arr, arr_len)
print(arr)
