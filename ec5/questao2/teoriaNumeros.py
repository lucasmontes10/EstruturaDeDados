def calculaNumero(n) :
    i = 0
    while (i * i <= n) :
        j = i
        while (j * j <= n) :
            k = j
            while (k * k <= n) :
                l = k
                while (l * l <= n) :
                    if (i * i + j * j + k * k + l * l == n) :        
                        print ("{} = {}*{} + {}*{} +".format(n,i,i,j,j), end = " ")
                        print ("{}*{} + {}*{}".format(k,k,l,l), end="\n")
                    l = l + 1
                k = k + 1
            j = j + 1
        i = i + 1
                    
n = int(input("Entre com o numero desejado: "))

calculaNumero(n)