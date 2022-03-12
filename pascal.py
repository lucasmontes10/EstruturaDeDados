def preencherMatiz(n, mat):
    for i in range(0, n):
        mat.append(0)
        mat[i] = []
        for j in range(0, n):
            mat[i].append(-1)

def printar_matriz(n, mat):
    for i in range(0, n):
        for j in range(0, n):
            if(mat[i][j] != -1):
                print(mat[i][j],end=' ')
        print('\n')

def construir_Pascal(n, mat):
    for i in range(0, n):
        for j in range(0, i + 1):
            if (i == j or j == 0): #preenchendo o primeiro e o ultimo valor
                mat[i][j] = 1
            else:
                # 1 2 1
                # 1 3 3 1
                mat[i][j] = mat[i-1][j-1] + mat[i-1][j]

n = int(input("Entre com a ordem da matriz:"))
mat = []
preencherMatiz(n, mat)
construir_Pascal(n, mat)
printar_matriz(n, mat)