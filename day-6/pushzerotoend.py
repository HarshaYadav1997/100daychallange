def pushzerotoend(array,n):
    count=0
    for i in range(n):
        if array[i]!=0:
            array[count]=array[i]
            count=count+1
    while count<n:
        array[count]=0
        count=count+1
array = [3, 0, 1, 0, 5, 9, 0, 6, 7]
n = len(array)
pushzerotoend(array, n)
print("Array after pushing all zeros to end of array:")
print(array)
