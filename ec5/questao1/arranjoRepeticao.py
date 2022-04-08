
def arranjoRepetido(np):
    global quant
    for i in range(1, n + 1):
        p[np] = i
        if (np == q):
            printarLista(p)
            if (quant == 100):
                exit()
            quant += 1
        else:
            arranjoRepetido(np + 1)

def printarLista(p):
    for i in range(1, len(p)):
        if(p[i] != -1):
            print(p[i], end = ' ')
    print("\n")

n = int(input("Entre com n:"))
q = 3
p = []
quant = 0
for i in range(0, n):
    p.append(-1)
arranjoRepetido(1)