num1= int(input("enter first no"))
num2 = int(input("enter second no"))
a = num1
b = num2
while(b!=0):
 temp = b
 b = a % b
 a = temp
print("hcf is",a)

lcm = (num1 * num2)/a
print("lcm is",lcm)
