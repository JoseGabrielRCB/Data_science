def Conta_100(a):
    soma = 0
    cont = 0
    while cont < len(a):
        soma += a[cont]
        cont +=1
        if (cont % 100 == 0):
            yield soma


conjunto  = list(range(1,501))
soma = Conta_100(conjunto)
print(list(soma))