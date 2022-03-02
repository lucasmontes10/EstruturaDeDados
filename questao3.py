def preencherVetor(moedas, n, peso, f):
    moedas.append(0)
    for i in range(1, n + 1):
        if (i == f):
            moedas.append(peso + 1)
        else:
            moedas.append(peso)
    if (n % 2 == 1):
        moedas.append(peso)
        
#Documentação moedas = [p....r]
# def medirMoedas(p, r, moedas):
#     if (p == r):
#         return moedas[r]  
#     else:
#         q = (r + p) // 2
#         print(p, "-", r, " X ")
#         x = medirMoedas(p, q, moedas)
#         print(p, "-", r, " Y ")
#         y = medirMoedas(q + 1, r, moedas)
#         if (x >=y ):
#             print("Entrei x")
#             return x
#         else:
#             print("Entrei Y")
#             return y
def medirMoedas(p, r, moedas, peso):
    if (p == r):
        return moedas[r]
    else: 
        q = (r + p) // 2
        somaesq = 0
        somadir = 0
        quant = 1
        if ((r - p) % 2 == 0):
            moedas.append(peso)
        for i in range(p, q + 1):
            somaesq += moedas[i]
            somadir += moedas[q + quant]
            quant += 1 
        if (somaesq > somadir):
            print(p, "-", q, " X ", q + 1, "-", r)
            return medirMoedas(p, q, moedas, peso)
        else:
            print(p, "-", q, " X ", q + 1, "-", r)
            return medirMoedas(q + 1, r, moedas, peso)


moedas = []
n = int(input("Entre com o numero de moedas "))
peso = int(input("Entre com o peso da moeda original: "))
f = int(input("Entre com a posicao da moeda falsa:"))
preencherVetor(moedas, n, peso, f)
posFalsa = medirMoedas(1, n, moedas, peso)
posFalsa = moedas.index(posFalsa)
# print(moedas)
print("\nA posicao da moeda falsa e igual a:", posFalsa)
# for i in range(1, n + 1):
#     print(moedas[i], " ")
