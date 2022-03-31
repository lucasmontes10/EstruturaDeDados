def geraSub(ns, t):
    for i in range(t, n + 1):
        s[ns] = i
        print(s)
        if (i < n):
            geraSub(ns + 1, i + 1)



n = int(input("Entre com a quantidade de elementos do subconjunto: "))
s = []
for i in range(0,10):
    s.append(0)

geraSub(1, 1)