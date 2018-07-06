
num =int(input("enter a no"))
print(num,end='')
print([i for i in range(1,num+1)
       if num%i==0])
