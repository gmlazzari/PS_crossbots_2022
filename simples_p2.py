def num_perfeito(n:int):
    '''
    Essa função verifica se um numero é  perfeito ou não.
    Um valor é dito perfeito quando ele é igual à soma dos seus divisores excetuando-o. 
    (ex: 6 é perfeito, 6 = 1 + 2 +3, que são seus divisores).
    E retorna True ou False.'''
    div_n = []
    for i in range(1,n):
        if(n%i == 0):
            div_n.append(i)
    
    if(sum(div_n) == n):
        return True
    else:
        return False
