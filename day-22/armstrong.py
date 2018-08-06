n = int(input("enter any number"))
originalnumber = n
result=0

while(originalnumber!=0):
    rem = originalnumber%10
    result += rem*rem*rem
    originalnumber //=10

if(result==n):
    print("no is armstrong")
else:
    print("no is not armstrong")
