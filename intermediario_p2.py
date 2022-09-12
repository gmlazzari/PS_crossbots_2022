def list_sem_rep(lista:list) ->list:
    '''
    Essa função recebe uma lista de numeros inteiros
    e imprime a lista sem numeros repetidos'''
    lista1 = []
    for i in lista:
        if(i not in lista1):
            lista1.append(i)
    
    print(lista1)

