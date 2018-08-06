n =int(input ('enter the no of rows,n= '))
m =int(input ('enter the no of coloumns, m= '))
matrix=[]; coloumn=[]
"initialize the no of row nd coloumn"
for i in  range(0,n):
 matrix+=[0]

for j in range(0,m):
 coloumn+=[0]

"initiakize the matrix"
for i in range(0,n):
    matrix[i]=coloumn
for i in range(0,n):
    for j in range(0,m):
        print('entry in row:',i+1,'coloumn: ', j+1)
        matrix[i][j] = int(input())
print (matrix)

 
