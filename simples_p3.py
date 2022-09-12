def encontra_primo(lista:list) ->list:
    '''
    Essa função recebe uma lista com inteiros e imprime
    outra lista com os primos contidos na lista recebida'''
    primos = []
    for i in lista:
        count = 0
        for j in range(1,i):
            if(i%j == 0):
                count += 1
        if(count == 1):
            primos.append(i)
    print(primos)

