X = [[18,17,33],
    [44 ,75,16],
    [17 ,78,69]]


result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
for i in range(len(X)):
   
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)
