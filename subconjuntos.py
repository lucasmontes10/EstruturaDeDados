def geraSub(ns, t):
    global n
    for i in range(t, n + 1):
        s[ns] = i
        printarSub()
        if (i < n):
            geraSub(ns + 1, i + 1)

def printarSub():
    global controlador
    aux = []
    print("{", end= ' ')
    for k in range(0, n + 1):
        if (s[k] != 0) and not (s[k] in aux):
            aux.append(s[k])
            print(s[k], end = ' ')
            matrizOrdenar[controlador][k] = s[k]
    print("}", end= '\n')
    controlador += 1


#colocando os elementos em uma matriz para tentar colocar em ordem 
def printarMatriz(lista, l, c):
    for i in range(0, l + 1):
        for j in range(0, c + 1):
            if (lista[i][j] != 0):
                print(lista[i][j],end=' ')
        print('\n')

def preencher_matriz(lista, l, c):
    for i in range(0, l + 1):
        lista.append(0)
        lista[i] = []
        for j in range(0, c + 1):
            lista[i].append(0)


n = int(input("Entre com a quantidade de elementos do subconjunto: "))
s = []
matrizOrdenar = []
preencher_matriz(matrizOrdenar, n * n, n)
for i in range(0, n + 1):
    s.append(0)
controlador = 0
geraSub(1, 1)
print("\n")
# printarMatriz(matrizOrdenar, n * n, n)