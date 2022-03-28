# add two matrices

mat1 = [[1,2,3],[1,2,3],[1,2,3]]
mat2 = [[1,2,3],[1,2,3],[1,2,3]]
res = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(mat1)):
    for j in range(len(mat2)):
        res[i][j] = mat1[i][j] + mat2[i][j]

print(res)