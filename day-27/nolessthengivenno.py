l = [2,15 ,1 ,45, 12,32,889.78,63,51,47,48,35,36]
num = int(input("enter any num"))
newlist=[]

for i in l:
    if(i<num):
      newlist.append(i)

print(newlist)
