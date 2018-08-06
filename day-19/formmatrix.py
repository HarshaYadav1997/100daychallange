row=int(input("enter the no of rows:"))
coloumn=int(input("enter the no of coloumns:"))
matrix=[]
for i in range(0,row):
   matrix.append([])
   for j in range(0,coloumn):
       matrix[i].append(0)
print(matrix)
