def missingelement(a,start,end):
    if(start>end):
        return end+1
    if (start!=a[start]):
        return start
    mid=int((start+end)/2)
    if (a[mid]==mid):
        return missingelement(a,mid+1,end)
        return missingelement(a,start,mid)

a=[int(i) for i in input("enter the number").strip().split()]
n=len(a)
print("missing element is ",missingelement(a,0,n-1))
       
