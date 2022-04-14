from math import floor


def frascoMinimo(w):
    total = 0
    t = len(p)
    for i in range(t - 1, 0, -1):
        x = floor(w / p[i])
        total  += x
        w = w - (x * p[i])
    return total

p = [1 , 5, 10, 25, 50] #numero de comprimidos que cada frasco pode conter
w = int(input("Entre com a quantidade de comprimido: "))
print("O numero minimo de frasco e: ", frascoMinimo(w))
