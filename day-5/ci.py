
p = float(input("enter the principal"))
r = float(input("enter the rate"))
t = float(input("enter the time"))

ci = p * (pow((1 + r / 100), t))
print("Compound Interest is %.2f" % round(ci,2))

    
             
