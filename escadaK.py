def calcularManeiras(n, k):
    if(n == 0):
        return 1
    if(n < 0):
        return 0
    if(memo[n] == 0):
        for i in range(1, k + 1):
            memo[n] += calcularManeiras(n-i, k)

    return memo[n]


n = int(input("Entre com o n: "))
memo = [0 for i in range(n+1)]

k = int(input("Entre com o k: "))

print(calcularManeiras(n, k))