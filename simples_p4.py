def encontra_letra(c,str:str) ->int:
    '''
    Essa função recebe um caractere e uma string e imprime o numero de
    vezes que esse caractere aparece na string recebida.'''
    count = 0
    for i in str:
        if(i == c):
            count += 1
    print(count)    

