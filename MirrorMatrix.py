m=int(input("Enter the no. of rows"))
n=int(input("Enter the no of columns"))
matrix=[]
for i in range(m):
    row=[]
    for j in range(n):
        element=int(input(f"Enter element at position ({i},{j}): "))
        row.append(element)
    matrix.append(row)
print("\n Original Matrix")
for i in range(m):
    for j in range(n):
        print(matrix[i][j],end="\t")
    print()
for i in range(m):
    for j in range(n//2):
        temp=matrix[i][j]
        matrix[i][j]=matrix[i][n-1-j]
        matrix[i][n-1-j]=temp
print("\n Mirrored Matrix")
for i in range(m):
    for j in range(n):
        print(matrix[i][j],end="\t")
    print()