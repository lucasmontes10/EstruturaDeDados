
def comb(np):
    global q
    global quant
    for i in range(1, n + 1):
        if (i > p[np - 1]):
            p[np] = i
            if (np == q):
                printarLista(p)
                if (quant == 100):
                    exit()
                quant += 1
            else:
                comb(np + 1)
                

def printarLista(p):
    for i in range(1, len(p)):
        if(p[i] != -1):
            print(p[i], end = ' ')
    print("\n")


n = int(input("Entre com o n:"))
q = int(input("Em quantos em quantos elementos: "))
p = []
quant = 0
for i in range(0, n + 1):
    #iniciando o vetor p
    p.append(-1) 
p[0] = 0
comb(1)