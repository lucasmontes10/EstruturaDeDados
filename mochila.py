def preencherMatiz(capacidade, i, mat):
    for k in range(0, i):
        mat.append(0)
        mat[k] = []
        for j in range(0, capacidade):
            mat[k].append(0)

def calcularMaximo(capacidade, i, mat, item):
    for k in range(1, i + 1):
        for j in range(1, capacidade + 1):
            if(item[i-1][1] > j):
                mat[i][j] = mat[i-1][j]
            else:
                mat[i][j] = max(mat[i-1][j], mat[i-1][j- item[i-1][1]] + item[i - 1][1])

def topDownMochila(capacidade, item):
    i = len(item)
    if(capacidade == 0 or i == 0):
        return 0
    if(item[i-1][1] > capacidade):
        return topDownMochila(capacidade, item[:i-1])

    return max(topDownMochila(capacidade, item[:i-1]), item[i-1][0] + topDownMochila(capacidade - item[i-1][1], item[:i-1]))


def printar_matriz(capacidade, n, mat):
    for i in range(0, n):
        for j in range(0, capacidade):
            if(mat[i][j] != -1):
                print(mat[i][j],end=' ')
        print('\n')




capacidade = int(13)
item = [[1, 2], [2, 4], [3, 7], [4, 8], [5, 12]]  # [valor, peso]
i = len(item)
mat = []
preencherMatiz(capacidade, i, mat)
calcularMaximo(capacidade, i, mat, item)
printar_matriz(capacidade, i, mat)
# printarMatriz(mat, capacidade, i)
# print(topDownMochila(capacidade, item))