def geraSub(ns, t):
    global n
    for i in range(t, n + 1):
        s[ns] = i
        printarSub()
        if (i < n):
            geraSub(ns + 1, i + 1)

def printarSub():
    aux = []
    print("{", end= ' ')
    for k in range(0, n + 1):
        if (s[k] != 0) and not (s[k] in aux):
            aux.append(s[k])
            print(s[k], end = ' ')
    print("}", end= '\n')


n = int(input("Entre com a quantidade de elementos do subconjunto: "))
s = []
for i in range(0, n + 1):
    s.append(0)

geraSub(1, 1)