num =int(input("Enter the number of items to be added : "))

mydata = dict(input("Item Name and Weight(In KG) : ").split() for _ in range(num))
f = open("grocerylist.txt","w")
f.write(str(mydata))
f.close()
myfile = eval(open("grocerylist.txt").read())
itemname=input("Enter item name you want to search :")
print("Items Details(Name and Weight) :: ",end='')
print(itemname.capitalize()+" => "+myfile[itemname]+" KG")
