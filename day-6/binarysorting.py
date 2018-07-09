def Array(arr, arr_len):
    j = -1
    for i in range(arr_len):
        if arr[i] < 1:
            j += 1
            
            arr[i], arr[j] = arr[j], arr[i]


arr = [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
print("Original Array : ",end='')
for i in arr:
    print(i,end=' ')
arr_len = len(arr)
Array(arr, arr_len)
print("\n\nSorted Array : ",end='')
for i in range(arr_len):
    print(arr[i], end=" ")
