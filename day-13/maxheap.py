def MaxHeapify(arr, i, arr_len):
    l = 2*i + 1
    r = 2*i + 2
    largest = i
    if l < arr_len and arr[l] > arr[i]:
        largest=l
    if r < arr_len and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        MaxHeapify(arr, largest, arr_len)


def convertMax(arr, arr_len):
    val = int((arr_len - 2) / 2)
    for i in range(val, -1, -1):
        MaxHeapify(arr, i, arr_len)


arr = [1, 3, 4, 6, 10, 8, 5]
arr_len = len(arr)
print("Min Heap Array : ",arr)
convertMax(arr, arr_len)
print("Max-Heap Array : ",arr)
