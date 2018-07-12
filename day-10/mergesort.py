def merge(left, right, arr):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def mergesort(arr):
    n = len(arr)
    if n < 2:
        return
    mid = n // 2
    left = []
    right = []
    for i in range(mid):
        number = arr[i]
        left.append(number)
    for i in range(mid, n):
        number = arr[i]
        right.append(number)
    mergesort(left)
    mergesort(right)
    merge(left, right, arr)


arr = [45, 28, 13, 97, 56, 78, 21, 90, 33, 62]
mergesort(arr)
print(arr)
