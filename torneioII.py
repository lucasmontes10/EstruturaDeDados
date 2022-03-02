def preencherMatiz(n, lista):
    for i in range(0, n+1):
        lista.append(0)
        lista[i] = []
        for j in range(0, n + 1):
            lista[i].append(0)

def printar_matriz(lista, n):
    for i in range(0, n+1):
        for j in range(0, n + 1):
            print(lista[i][j],end=' ')
        print('\n')

def torneio(m, mat):
    if(m == 1):
        mat[1][1] = 1
    else:
        p = m // 2
        torneio(p, mat)
        for i in range(1, p + 1):
            for j in range(1, p + 1):
                mat[i+p][j] = mat[i][j] + p
                # mat[i][j+p] = p + 1 + (i + j - 2) % p
                # mat[p + 1 + (i + j - 2) % p][j + p] = i
                mat[i][j+p] = m - (j - i + m) % p
                mat[m - (j - i + m) % p][j + p] = i


m = int(input("Entre com o numero de times: "))
mat = []
preencherMatiz(m, mat)
torneio(m, mat)
printar_matriz(mat, m)