# 05/11/24
# Rotate by 90 degree

def rotate(mat):
    m = len(mat)
    for i in range(m//2):
        for j in range(i,m-i-1):
            temp = mat[i][j]
            mat[i][j] = mat[m-j-1][i]
            mat[m-j-1][i] = mat[m-i-1][m-j-1]
            mat[m-i-1][m-j-1] = mat[j][m-i-1]
            mat[j][m-i-1] = temp
    return mat