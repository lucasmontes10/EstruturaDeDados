def minMax(inicio, fim, lista):
    if (inicio == fim):
        return lista[inicio], lista[inicio]
    elif (fim == inicio + 1):
        if (lista[inicio] < lista[fim]):
            return lista[inicio], lista[fim]
        else:
            return lista[fim], lista[inicio]
    else:
        m = (inicio + fim) // 2
        a1, b1 = minMax(inicio, m, lista)
        a2, b2 = minMax(m + 1, fim, lista)
        return (min(a1, a2)), (max(b1, b2))



listaNumeros = [15, 20, 30, 10, 9, 40, 45]
inicio = 0
fim = len(listaNumeros) - 1
min, max = minMax(inicio, fim, listaNumeros)
print("min = ", min, " max = ", max)