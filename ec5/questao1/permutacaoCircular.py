def permCircular(np):
    global n
    global quant
    for i in range(1, n):
        if (not s[i]):
            p[np] = i
            s[i] = True
            if np == n - 1:
                printarLista(p)
                #printando as 100 primeiras ocorrências
                if (quant == 100):
                    exit()
                quant += 1
            else:
                permCircular(np + 1)
            s[i] = False

def printarLista(p):
    for i in range(1, len(p)):
        if(p[i] != -1):
            print(p[i], end = ' ')
    print("\n")



n = int(input("Entre com o valor de n:"))
s = []
p = []
quant = 0
for i in range(0, n + 1):
    s.append(False)
    p.append(-1)
p[n] = n
permCircular(1)