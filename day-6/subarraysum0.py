num=int(input("Enter the number of elements in array : "))
arr = []
subarray=[[]]

for i in range(num):
    arr.append(int(input()))
arr_len=len(arr)
print("Original Array : "+str(arr))

for i in range(arr_len):
    for j in range(i+1,arr_len+1):
        sub_ele=arr[i:j]
        subarray.append(sub_ele)

print("Sub-array(s) having sum Zero : ")
for sub in subarray:
    sum = 0
    for l in range(len(sub)):
        sum+=sub[l]
    if(sum == 0  and len(sub)>0):
        print(sub)


      
      
