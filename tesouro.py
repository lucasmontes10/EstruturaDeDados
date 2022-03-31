#função para calcular o numero max de tesouro

def calcularTesouros(tempo, tesouro):
    tamanho = len(tesouro)
    #fazendo operações semelhantes ao algoritmo da mochila
    if ((tamanho == 0) or tempo == 0):
        memo[tamanho - 1] = 0
        return 0
    #para pegar um tesouro precisamos garantir que o tempo submerso
    #é maior que o tempo necessário que é 9 * profundidade
    if(tempo <  9 * tesouro[tamanho - 1]):
        #caso eu nn consiga pegar o tesouro, tempo comparado com 9 vezes a profundidade
        memo [tamanho - 1] = calcularTesouros(tempo, tesouro[:tamanho - 1])
        #nesse caso queremos todos os valores anteriores, nesse caso usamos tesouro[:i-1]
        #ele nn pega o extremo, ou seja, o valor tamanho - 1  não irá entrar
        return memo[tamanho - 1]
    #caso eu consiga verifico qual é maior das duas 
    memo[tamanho - 1] = max(calcularTesouros(tempo, tesouro[:tamanho - 1]), tesouro[tamanho - 1] + calcularTesouros(tempo - 9*tesouro[tamanho - 1], tesouro[:tamanho - 1]))
    return memo[tamanho - 1]

# def printarTesouro(tesouro):
#     tamanho = len(tesouro)
#     for i in range(0, tamanho):
#         if (memo[i] != -1):
#             print("tesouro:", memo[i], end = ' ')

#criando a matriz que irá representar os tesouros, analogamente com o da mochila, em que 
#tinha os valores e o peso, aqui a primeira irá representar a profundidade e a quantidade de ouro
tesouro = [3,10,4,6,8]

#usuario vai entrar com tempo que ficará submerso, ou seja, o tempo do cilindro de ar
#análogo ao w no problema da mochila 
k = 19
#vetor de memorização
memo = []
for i in range(0, len(tesouro)):
    memo.append(-1)
print("O numero maximo do tesouro (ouro) e igual a: ", calcularTesouros(k, tesouro))
# printarTesouro(tesouro)
