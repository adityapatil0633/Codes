# matrix add of 2
print("enter rows m and columns n:")
m = int(input("enter no.of rows M:"))
n = int(input("enter no.of columns N:"))

matrix1=[]
matrix2=[]

print("enter element of first matrix :")
for i in range(m):
    row = []
    for j in range(n):
        new =int(input("enter one element:"))
        row.append(new)
        matrix1.append(row)


print("enter elements of second  matrix:")
for i in range(m):
    row =[]
    for j in range(n):
        new =int(input("enter one element:"))
        row.append(new)
        matrix2.append(row)
        
print("Matrix1:",matrix1)
print("Matrix2:",matrix2)

matrix3=[]
for i in range(m):
    row=[]
    for j in range(n):
     new3 = matrix1[i][j] + matrix2[i][j]
     row.append(new3)
     matrix3.append(row)
        
print("addition of two matrix:",matrix3) 