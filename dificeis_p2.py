def switch(c): #Funçao que marca o casas ocupadas pelas peças brancas
    if(c == '.' or c == 'k'):
        return "*"
    else:
        return c

def switch2(c): #Funçao que marca o casas ocupadas pelas peças pretas
    if(c == '.' or c == 'K'):
        return "*"
    else:
        return c


jogos = 1
while(True):
    #Transformar o input do tabuleiro em uma matriz
    tabuleiro = []
    for i in range(8):
        Input = input("")
        if(len(Input) == 0):
            Input = input("")
        row = []
        for j in Input:
            row.append(j)
        tabuleiro.append(row)


    for i in tabuleiro: #caso uma linha em branco entre no tabuleiro
        if(len(i) == 0):
            tabuleiro.pop(i)
            
    tabuleiro2 = []
    tabuleiro2 = tabuleiro #tabuleiro 2 serve para checar o xeque das duas cores
    
    
    #Encontra a posição dos reis / Condição de parada
    casa_K = []
    casa_k = []
    count = 0
    for i in range(8):
        for j in range(8):
            if(tabuleiro[i][j] == 'K'): #Casa do Rei Branco
                casa_K = [i,j]
            elif(tabuleiro[i][j] == 'k'): #Casa do Rei Preto
                casa_k = [i,j]
            elif(tabuleiro[i][j] == '.'): #Contagem de espaços vazios para verificação de parada do programa
                count += 1 
    
    if(count == 64): #verificação da condição de parada do programa
        break
    
    
    # Movimentos das Peças / espaços "ocupados" / Verificação de xeque
    
    #Espaços "ocupados" pelas peças brancas
    for i in range(8):
        for j in range(8):
            if(tabuleiro[i][j] == 'P'): #Movimentos Peão branco
                if(j == 0 and i != 0):
                    tabuleiro[i-1][j+1] = switch(tabuleiro[i-1][j+1]) 
                elif(j == 7 and i != 0):
                    tabuleiro[i-1][j-1] = switch(tabuleiro[i-1][j-1])      
                elif(i != 0):
                    tabuleiro[i-1][j-1] = switch(tabuleiro[i-1][j-1])
                    tabuleiro[i-1][j+1] = switch(tabuleiro[i-1][j+1])                                             
            elif(tabuleiro[i][j] == 'B'): #Movimentos Bispo
                    I = i+1
                    J = j+1
                    while (I < 8 and J < 8):
                        tabuleiro[I][J] = switch(tabuleiro[I][J])
                        if(tabuleiro[I][J] != '.' and tabuleiro[I][J] != '*'):
                            break
                        I += 1    
                        J += 1
                    I = i+1
                    J = j-1
                    while (I < 8 and J >= 0):
                        tabuleiro[I][J] = switch(tabuleiro[I][J])
                        if(tabuleiro[I][J] != '.' and tabuleiro[I][J] != '*'):
                            break
                        I += 1    
                        J -= 1
                    I = i-1
                    J = j+1
                    while (I >= 0 and J < 8):
                        tabuleiro[I][J] = switch(tabuleiro[I][J])
                        if(tabuleiro[I][J] != '.' and tabuleiro[I][J] != '*'):
                            break
                        I -= 1    
                        J += 1
                    I = i-1
                    J = j-1
                    while (I >= 0 and J >= 0):
                        tabuleiro[I][J] = switch(tabuleiro[I][J])
                        if(tabuleiro[I][J] != '.' and tabuleiro[I][J] != '*'):
                            break
                        I -= 1    
                        J -= 1
            elif(tabuleiro[i][j] == 'N'): #Movimentos Cavalo
                if(i == 0):
                    if(j == 0):
                        tabuleiro[i+2][j+1] = switch(tabuleiro[i+2][j+1])
                        tabuleiro[i+1][j+2] = switch(tabuleiro[i+1][j+2])
                    elif(j == 1):
                        tabuleiro[i+2][j-1] = switch(tabuleiro[i+2][j+2])
                        tabuleiro[i+2][j+1] = switch(tabuleiro[i+2][j+1])
                        tabuleiro[i+1][j+2] = switch(tabuleiro[i+1][j-1])
                    elif(j == 6):
                        tabuleiro[i+2][j-1] = switch(tabuleiro[i+2][j-1])
                        tabuleiro[i+2][j+1] = switch(tabuleiro[i+2][j-1])
                        tabuleiro[i+1][j-2] = switch(tabuleiro[i+1][j-2])
                    elif(j == 7):
                        tabuleiro[i+2][j-1] = switch(tabuleiro[i+2][j-1])
                        tabuleiro[i+1][j-2] = switch(tabuleiro[i+1][j-2])
                    else:
                        tabuleiro[i+2][j-1] = switch(tabuleiro[i+2][j-1])
                        tabuleiro[i+2][j+1] = switch(tabuleiro[i+2][j-1])
                        tabuleiro[i+1][j-2] = switch(tabuleiro[i+1][j-2])   
                        tabuleiro[i+1][j+2] = switch(tabuleiro[i+1][j+2])                  
                elif(i == 1):
                    if(j == 0):
                        tabuleiro[i+2][j+1] = switch(tabuleiro[i+2][j+1])
                        tabuleiro[i+1][j+2] = switch(tabuleiro[i+1][j+2])
                        tabuleiro[i-1][j+2] = switch(tabuleiro[i-1][j+2])
                    elif(j == 1):
                        tabuleiro[i+2][j-1] = switch(tabuleiro[i+2][j+2])
                        tabuleiro[i+2][j+1] = switch(tabuleiro[i+2][j+1])
                        tabuleiro[i+1][j+2] = switch(tabuleiro[i+1][j-1])
                        tabuleiro[i-1][j+2] = switch(tabuleiro[i-1][j+2])
                    elif(j == 6):
                        tabuleiro[i+2][j-1] = switch(tabuleiro[i+2][j-1])
                        tabuleiro[i+2][j+1] = switch(tabuleiro[i+2][j-1])
                        tabuleiro[i+1][j-2] = switch(tabuleiro[i+1][j-2])
                        tabuleiro[i-1][j-2] = switch(tabuleiro[i-1][j-2])
                    elif(j == 7):
                        tabuleiro[i+2][j-1] = switch(tabuleiro[i+2][j-1])
                        tabuleiro[i+1][j-2] = switch(tabuleiro[i+1][j-2])
                        tabuleiro[i-1][j-2] = switch(tabuleiro[i-1][j-2])
                    else:
                        tabuleiro[i-1][j-2] = switch(tabuleiro[i-1][j-2])   
                        tabuleiro[i-1][j+2] = switch(tabuleiro[i-1][j+2])  
                        tabuleiro[i+2][j-1] = switch(tabuleiro[i+2][j-1])
                        tabuleiro[i+2][j+1] = switch(tabuleiro[i+2][j-1])
                        tabuleiro[i+1][j-2] = switch(tabuleiro[i+1][j-2])   
                        tabuleiro[i+1][j+2] = switch(tabuleiro[i+1][j+2])  
                elif(i == 6):
                    if(j == 0):
                        tabuleiro[i+1][j+2] = switch(tabuleiro[i+1][j+2])
                        tabuleiro[i-1][j+2] = switch(tabuleiro[i-1][j+2])
                        tabuleiro[i-2][j+1] = switch(tabuleiro[i-2][j+1])
                    elif(j == 1):
                        tabuleiro[i+1][j+2] = switch(tabuleiro[i+1][j-1])
                        tabuleiro[i-1][j+2] = switch(tabuleiro[i-1][j+2])
                        tabuleiro[i-2][j+1] = switch(tabuleiro[i-2][j+1])
                        tabuleiro[i-2][j-1] = switch(tabuleiro[i-2][j-1])
                    elif(j == 6):
                        tabuleiro[i+1][j-2] = switch(tabuleiro[i+1][j-2])
                        tabuleiro[i-1][j-2] = switch(tabuleiro[i-1][j-2])
                        tabuleiro[i-2][j+1] = switch(tabuleiro[i-2][j+1])
                        tabuleiro[i-2][j-1] = switch(tabuleiro[i-2][j-1])
                    elif(j == 7):
                        tabuleiro[i+1][j-2] = switch(tabuleiro[i+1][j-2])
                        tabuleiro[i-1][j-2] = switch(tabuleiro[i-1][j-2])
                        tabuleiro[i-2][j-1] = switch(tabuleiro[i-2][j-1])
                    else:
                        tabuleiro[i-2][j-1] = switch(tabuleiro[i-2][j-1])   
                        tabuleiro[i-2][j+1] = switch(tabuleiro[i-2][j+1])
                        tabuleiro[i-1][j-2] = switch(tabuleiro[i-1][j-2])   
                        tabuleiro[i-1][j+2] = switch(tabuleiro[i-1][j+2])  
                        tabuleiro[i+1][j-2] = switch(tabuleiro[i+1][j-2])   
                        tabuleiro[i+1][j+2] = switch(tabuleiro[i+1][j+2]) 
                elif(i == 7):
                    if(j == 0):
                        tabuleiro[i-1][j+2] = switch(tabuleiro[i-1][j+2])
                        tabuleiro[i-2][j+1] = switch(tabuleiro[i-2][j+1])
                    elif(j == 1):
                        tabuleiro[i-1][j+2] = switch(tabuleiro[i-1][j+2])
                        tabuleiro[i-2][j+1] = switch(tabuleiro[i-2][j+1])
                        tabuleiro[i-2][j-1] = switch(tabuleiro[i-2][j-1])
                    elif(j == 6):
                        tabuleiro[i-1][j-2] = switch(tabuleiro[i-1][j-2])
                        tabuleiro[i-2][j+1] = switch(tabuleiro[i-2][j+1])
                        tabuleiro[i-2][j-1] = switch(tabuleiro[i-2][j-1])
                    elif(j == 7):
                        tabuleiro[i-1][j-2] = switch(tabuleiro[i-1][j-2])
                        tabuleiro[i-2][j-1] = switch(tabuleiro[i-2][j-1])
                    else:
                        tabuleiro[i-2][j-1] = switch(tabuleiro[i-2][j-1])   
                        tabuleiro[i-2][j+1] = switch(tabuleiro[i-2][j+1])
                        tabuleiro[i-1][j-2] = switch(tabuleiro[i-1][j-2])   
                        tabuleiro[i-1][j+2] = switch(tabuleiro[i-1][j+2])                
                else:
                    if(j == 0):
                        tabuleiro[i+2][j+1] = switch(tabuleiro[i+2][j+1])
                        tabuleiro[i+1][j+2] = switch(tabuleiro[i+1][j+2])
                        tabuleiro[i-1][j+2] = switch(tabuleiro[i-1][j+2])
                        tabuleiro[i-2][j+1] = switch(tabuleiro[i-2][j+1])
                    elif(j == 1):
                        tabuleiro[i+2][j+1] = switch(tabuleiro[i+2][j+1])
                        tabuleiro[i+2][j-1] = switch(tabuleiro[i+2][j-1])
                        tabuleiro[i+1][j+2] = switch(tabuleiro[i+1][j-1])
                        tabuleiro[i-1][j+2] = switch(tabuleiro[i-1][j+2])
                        tabuleiro[i-2][j+1] = switch(tabuleiro[i-2][j+1])
                        tabuleiro[i-2][j-1] = switch(tabuleiro[i-2][j-1])
                    elif(j == 6):
                        tabuleiro[i+2][j+1] = switch(tabuleiro[i+2][j+1])
                        tabuleiro[i+2][j-1] = switch(tabuleiro[i+2][j-1])                    
                        tabuleiro[i+1][j-2] = switch(tabuleiro[i+1][j-2])
                        tabuleiro[i-1][j-2] = switch(tabuleiro[i-1][j-2])
                        tabuleiro[i-2][j+1] = switch(tabuleiro[i-2][j+1])
                        tabuleiro[i-2][j-1] = switch(tabuleiro[i-2][j-1])
                    elif(j == 7):
                        tabuleiro[i+2][j-1] = switch(tabuleiro[i+2][j-1])                    
                        tabuleiro[i+1][j-2] = switch(tabuleiro[i+1][j-2])
                        tabuleiro[i-1][j-2] = switch(tabuleiro[i-1][j-2])
                        tabuleiro[i-2][j-1] = switch(tabuleiro[i-2][j-1])
                    else:
                        tabuleiro[i-2][j-1] = switch(tabuleiro[i-2][j-1])   
                        tabuleiro[i-2][j+1] = switch(tabuleiro[i-2][j+1])
                        tabuleiro[i-1][j-2] = switch(tabuleiro[i-1][j-2])   
                        tabuleiro[i-1][j+2] = switch(tabuleiro[i-1][j+2])  
                        tabuleiro[i+1][j-2] = switch(tabuleiro[i+1][j-2])   
                        tabuleiro[i+1][j+2] = switch(tabuleiro[i+1][j+2])
                        tabuleiro[i+2][j-1] = switch(tabuleiro[i+2][j-1])
                        tabuleiro[i+2][j+1] = switch(tabuleiro[i+2][j-1])                
            elif(tabuleiro[i][j] == 'R'): #Movimentos Torre
                    I = i+1
                    J = j
                    while (I < 8):
                        tabuleiro[I][J] = switch(tabuleiro[I][J])
                        if(tabuleiro[I][J] != '.' and tabuleiro[I][J] != '*'):
                            break
                        I += 1    
                    I = i-1
                    J = j
                    while (I >= 0):
                        tabuleiro[I][J] = switch(tabuleiro[I][J])
                        if(tabuleiro[I][J] != '.' and tabuleiro[I][J] != '*'):
                            break
                        I -= 1    
                    J = j+1
                    I = i
                    while (J < 8):
                        tabuleiro[I][J] = switch(tabuleiro[I][J])
                        if(tabuleiro[I][J] != '.' and tabuleiro[I][J] != '*'):
                            break
                        J += 1
                    J = j-1
                    I = i
                    while (J >= 0):
                        tabuleiro[I][J] = switch(tabuleiro[I][J])
                        if(tabuleiro[I][J] != '.' and tabuleiro[I][J] != '*'):
                            break   
                        J -= 1
            elif(tabuleiro[i][j] == 'Q'): #Movimentos Rainha
                    I = i+1
                    J = j+1
                    while (I < 8 and J < 8):
                        tabuleiro[I][J] = switch(tabuleiro[I][J])
                        if(tabuleiro[I][J] != '.' and tabuleiro[I][J] != '*'):
                            break
                        I += 1    
                        J += 1
                    I = i+1
                    J = j-1
                    while (I < 8 and J >= 0):
                        tabuleiro[I][J] = switch(tabuleiro[I][J])
                        if(tabuleiro[I][J] != '.' and tabuleiro[I][J] != '*'):
                            break
                        I += 1    
                        J -= 1
                    I = i-1
                    J = j+1
                    while (I >= 0 and J < 8):
                        tabuleiro[I][J] = switch(tabuleiro[I][J])
                        if(tabuleiro[I][J] != '.' and tabuleiro[I][J] != '*'):
                            break
                        I -= 1    
                        J += 1
                    I = i-1
                    J = j-1
                    while (I >= 0 and J >= 0):
                        tabuleiro[I][J] = switch(tabuleiro[I][J])
                        if(tabuleiro[I][J] != '.' and tabuleiro[I][J] != '*'):
                            break
                        I -= 1    
                        J -= 1
                    I = i+1
                    J = j
                    while (I < 8):
                        tabuleiro[I][J] = switch(tabuleiro[I][J])
                        if(tabuleiro[I][J] != '.' and tabuleiro[I][J] != '*'):
                            break
                        I += 1    
                    I = i-1
                    J = j
                    while (I >= 0):
                        tabuleiro[I][J] = switch(tabuleiro[I][J])
                        if(tabuleiro[I][J] != '.' and tabuleiro[I][J] != '*'):
                            break
                        I -= 1    
                    J = j+1
                    I = i
                    while (J < 8):
                        tabuleiro[I][J] = switch(tabuleiro[I][J])
                        if(tabuleiro[I][J] != '.' and tabuleiro[I][J] != '*'):
                            break
                        J += 1
                    J = j-1
                    I = i
                    while (J >= 0):
                        tabuleiro[I][J] = switch(tabuleiro[I][J])
                        if(tabuleiro[I][J] != '.' and tabuleiro[I][J] != '*'):
                            break   
                        J -= 1  
    
    #Verificação se o rei preto esta em xeque
    if(tabuleiro[casa_k[0]][casa_k[1]] == '*'):
        jogos += 1
        print(f"Jogo #{jogos}: O rei preto esta em xeque")
        continue

    #Espaços "ocupados" pelas peças pretas
    for i in range(8):
        for j in range(8):
            if(tabuleiro2[i][j] == 'p'): #Movimentos Peão preto
                if(j == 0 and i != 0):
                    tabuleiro2[i+1][j+1] = switch2(tabuleiro2[i-1][j+1]) 
                elif(j == 7 and i != 0):
                    tabuleiro2[i+1][j-1] = switch2(tabuleiro2[i-1][j-1])      
                elif(i != 0):
                    tabuleiro2[i+1][j-1] = switch2(tabuleiro2[i-1][j-1])
                    tabuleiro2[i+1][j+1] = switch2(tabuleiro2[i-1][j+1])                                             
            elif(tabuleiro2[i][j] == 'b'): #Movimentos Bispo
                    I = i+1
                    J = j+1
                    while (I < 8 and J < 8):
                        tabuleiro2[I][J] = switch2(tabuleiro2[I][J])
                        if(tabuleiro2[I][J] != '.' and tabuleiro2[I][J] != '*'):
                            break
                        I += 1    
                        J += 1
                    I = i+1
                    J = j-1
                    while (I < 8 and J >= 0):
                        tabuleiro2[I][J] = switch2(tabuleiro2[I][J])
                        if(tabuleiro2[I][J] != '.' and tabuleiro2[I][J] != '*'):
                            break
                        I += 1    
                        J -= 1
                    I = i-1
                    J = j+1
                    while (I >= 0 and J < 8):
                        tabuleiro2[I][J] = switch2(tabuleiro2[I][J])
                        if(tabuleiro2[I][J] != '.' and tabuleiro2[I][J] != '*'):
                            break
                        I -= 1    
                        J += 1
                    I = i-1
                    J = j-1
                    while (I >= 0 and J >= 0):
                        tabuleiro2[I][J] = switch2(tabuleiro2[I][J])
                        if(tabuleiro2[I][J] != '.' and tabuleiro2[I][J] != '*'):
                            break
                        I -= 1    
                        J -= 1
            elif(tabuleiro2[i][j] == 'n'): #Movimentos Cavalo
                if(i == 0):
                    if(j == 0):
                        tabuleiro2[i+2][j+1] = switch2(tabuleiro2[i+2][j+1])
                        tabuleiro2[i+1][j+2] = switch2(tabuleiro2[i+1][j+2])
                    elif(j == 1):
                        tabuleiro2[i+2][j-1] = switch2(tabuleiro2[i+2][j+2])
                        tabuleiro2[i+2][j+1] = switch2(tabuleiro2[i+2][j+1])
                        tabuleiro2[i+1][j+2] = switch2(tabuleiro2[i+1][j-1])
                    elif(j == 6):
                        tabuleiro2[i+2][j-1] = switch2(tabuleiro2[i+2][j-1])
                        tabuleiro2[i+2][j+1] = switch2(tabuleiro2[i+2][j-1])
                        tabuleiro2[i+1][j-2] = switch2(tabuleiro2[i+1][j-2])
                    elif(j == 7):
                        tabuleiro2[i+2][j-1] = switch2(tabuleiro2[i+2][j-1])
                        tabuleiro2[i+1][j-2] = switch2(tabuleiro2[i+1][j-2])
                    else:
                        tabuleiro2[i+2][j-1] = switch2(tabuleiro2[i+2][j-1])
                        tabuleiro2[i+2][j+1] = switch2(tabuleiro2[i+2][j-1])
                        tabuleiro2[i+1][j-2] = switch2(tabuleiro2[i+1][j-2])   
                        tabuleiro2[i+1][j+2] = switch2(tabuleiro2[i+1][j+2])                  
                elif(i == 1):
                    if(j == 0):
                        tabuleiro2[i+2][j+1] = switch2(tabuleiro2[i+2][j+1])
                        tabuleiro2[i+1][j+2] = switch2(tabuleiro2[i+1][j+2])
                        tabuleiro2[i-1][j+2] = switch2(tabuleiro2[i-1][j+2])
                    elif(j == 1):
                        tabuleiro2[i+2][j-1] = switch2(tabuleiro2[i+2][j+2])
                        tabuleiro2[i+2][j+1] = switch2(tabuleiro2[i+2][j+1])
                        tabuleiro2[i+1][j+2] = switch2(tabuleiro2[i+1][j-1])
                        tabuleiro2[i-1][j+2] = switch2(tabuleiro2[i-1][j+2])
                    elif(j == 6):
                        tabuleiro2[i+2][j-1] = switch2(tabuleiro2[i+2][j-1])
                        tabuleiro2[i+2][j+1] = switch2(tabuleiro2[i+2][j-1])
                        tabuleiro2[i+1][j-2] = switch2(tabuleiro2[i+1][j-2])
                        tabuleiro2[i-1][j-2] = switch2(tabuleiro2[i-1][j-2])
                    elif(j == 7):
                        tabuleiro2[i+2][j-1] = switch2(tabuleiro2[i+2][j-1])
                        tabuleiro2[i+1][j-2] = switch2(tabuleiro2[i+1][j-2])
                        tabuleiro2[i-1][j-2] = switch2(tabuleiro2[i-1][j-2])
                    else:
                        tabuleiro2[i-1][j-2] = switch2(tabuleiro2[i-1][j-2])   
                        tabuleiro2[i-1][j+2] = switch2(tabuleiro2[i-1][j+2])  
                        tabuleiro2[i+2][j-1] = switch2(tabuleiro2[i+2][j-1])
                        tabuleiro2[i+2][j+1] = switch2(tabuleiro2[i+2][j-1])
                        tabuleiro2[i+1][j-2] = switch2(tabuleiro2[i+1][j-2])   
                        tabuleiro2[i+1][j+2] = switch2(tabuleiro2[i+1][j+2])  
                elif(i == 6):
                    if(j == 0):
                        tabuleiro2[i+1][j+2] = switch2(tabuleiro2[i+1][j+2])
                        tabuleiro2[i-1][j+2] = switch2(tabuleiro2[i-1][j+2])
                        tabuleiro2[i-2][j+1] = switch2(tabuleiro2[i-2][j+1])
                    elif(j == 1):
                        tabuleiro2[i+1][j+2] = switch2(tabuleiro2[i+1][j-1])
                        tabuleiro2[i-1][j+2] = switch2(tabuleiro2[i-1][j+2])
                        tabuleiro2[i-2][j+1] = switch2(tabuleiro2[i-2][j+1])
                        tabuleiro2[i-2][j-1] = switch2(tabuleiro2[i-2][j-1])
                    elif(j == 6):
                        tabuleiro2[i+1][j-2] = switch2(tabuleiro2[i+1][j-2])
                        tabuleiro2[i-1][j-2] = switch2(tabuleiro2[i-1][j-2])
                        tabuleiro2[i-2][j+1] = switch2(tabuleiro2[i-2][j+1])
                        tabuleiro2[i-2][j-1] = switch2(tabuleiro2[i-2][j-1])
                    elif(j == 7):
                        tabuleiro2[i+1][j-2] = switch2(tabuleiro2[i+1][j-2])
                        tabuleiro2[i-1][j-2] = switch2(tabuleiro2[i-1][j-2])
                        tabuleiro2[i-2][j-1] = switch2(tabuleiro2[i-2][j-1])
                    else:
                        tabuleiro2[i-2][j-1] = switch2(tabuleiro2[i-2][j-1])   
                        tabuleiro2[i-2][j+1] = switch2(tabuleiro2[i-2][j+1])
                        tabuleiro2[i-1][j-2] = switch2(tabuleiro2[i-1][j-2])   
                        tabuleiro2[i-1][j+2] = switch2(tabuleiro2[i-1][j+2])  
                        tabuleiro2[i+1][j-2] = switch2(tabuleiro2[i+1][j-2])   
                        tabuleiro2[i+1][j+2] = switch2(tabuleiro2[i+1][j+2]) 
                elif(i == 7):
                    if(j == 0):
                        tabuleiro2[i-1][j+2] = switch2(tabuleiro2[i-1][j+2])
                        tabuleiro2[i-2][j+1] = switch2(tabuleiro2[i-2][j+1])
                    elif(j == 1):
                        tabuleiro2[i-1][j+2] = switch2(tabuleiro2[i-1][j+2])
                        tabuleiro2[i-2][j+1] = switch2(tabuleiro2[i-2][j+1])
                        tabuleiro2[i-2][j-1] = switch2(tabuleiro2[i-2][j-1])
                    elif(j == 6):
                        tabuleiro2[i-1][j-2] = switch2(tabuleiro2[i-1][j-2])
                        tabuleiro2[i-2][j+1] = switch2(tabuleiro2[i-2][j+1])
                        tabuleiro2[i-2][j-1] = switch2(tabuleiro2[i-2][j-1])
                    elif(j == 7):
                        tabuleiro2[i-1][j-2] = switch2(tabuleiro2[i-1][j-2])
                        tabuleiro2[i-2][j-1] = switch2(tabuleiro2[i-2][j-1])
                    else:
                        tabuleiro2[i-2][j-1] = switch2(tabuleiro2[i-2][j-1])   
                        tabuleiro2[i-2][j+1] = switch2(tabuleiro2[i-2][j+1])
                        tabuleiro2[i-1][j-2] = switch2(tabuleiro2[i-1][j-2])   
                        tabuleiro2[i-1][j+2] = switch2(tabuleiro2[i-1][j+2])                
                else:
                    if(j == 0):
                        tabuleiro2[i+2][j+1] = switch2(tabuleiro2[i+2][j+1])
                        tabuleiro2[i+1][j+2] = switch2(tabuleiro2[i+1][j+2])
                        tabuleiro2[i-1][j+2] = switch2(tabuleiro2[i-1][j+2])
                        tabuleiro2[i-2][j+1] = switch2(tabuleiro2[i-2][j+1])
                    elif(j == 1):
                        tabuleiro2[i+2][j+1] = switch2(tabuleiro2[i+2][j+1])
                        tabuleiro2[i+2][j-1] = switch2(tabuleiro2[i+2][j-1])
                        tabuleiro2[i+1][j+2] = switch2(tabuleiro2[i+1][j-1])
                        tabuleiro2[i-1][j+2] = switch2(tabuleiro2[i-1][j+2])
                        tabuleiro2[i-2][j+1] = switch2(tabuleiro2[i-2][j+1])
                        tabuleiro2[i-2][j-1] = switch2(tabuleiro2[i-2][j-1])
                    elif(j == 6):
                        tabuleiro2[i+2][j+1] = switch2(tabuleiro2[i+2][j+1])
                        tabuleiro2[i+2][j-1] = switch2(tabuleiro2[i+2][j-1])                    
                        tabuleiro2[i+1][j-2] = switch2(tabuleiro2[i+1][j-2])
                        tabuleiro2[i-1][j-2] = switch2(tabuleiro2[i-1][j-2])
                        tabuleiro2[i-2][j+1] = switch2(tabuleiro2[i-2][j+1])
                        tabuleiro2[i-2][j-1] = switch2(tabuleiro2[i-2][j-1])
                    elif(j == 7):
                        tabuleiro2[i+2][j-1] = switch2(tabuleiro2[i+2][j-1])                    
                        tabuleiro2[i+1][j-2] = switch2(tabuleiro2[i+1][j-2])
                        tabuleiro2[i-1][j-2] = switch2(tabuleiro2[i-1][j-2])
                        tabuleiro2[i-2][j-1] = switch2(tabuleiro2[i-2][j-1])
                    else:
                        tabuleiro2[i-2][j-1] = switch2(tabuleiro2[i-2][j-1])   
                        tabuleiro2[i-2][j+1] = switch2(tabuleiro2[i-2][j+1])
                        tabuleiro2[i-1][j-2] = switch2(tabuleiro2[i-1][j-2])   
                        tabuleiro2[i-1][j+2] = switch2(tabuleiro2[i-1][j+2])  
                        tabuleiro2[i+1][j-2] = switch2(tabuleiro2[i+1][j-2])   
                        tabuleiro2[i+1][j+2] = switch2(tabuleiro2[i+1][j+2])
                        tabuleiro2[i+2][j-1] = switch2(tabuleiro2[i+2][j-1])
                        tabuleiro2[i+2][j+1] = switch2(tabuleiro2[i+2][j-1])                
            elif(tabuleiro[i][j] == 'r'): #Movimentos Torre
                    I = i+1
                    J = j
                    while (I < 8):
                        tabuleiro2[I][J] = switch2(tabuleiro2[I][J])
                        if(tabuleiro2[I][J] != '.' and tabuleiro2[I][J] != '*'):
                            break
                        I += 1    
                    I = i-1
                    J = j
                    while (I >= 0):
                        tabuleiro2[I][J] = switch2(tabuleiro2[I][J])
                        if(tabuleiro2[I][J] != '.' and tabuleiro2[I][J] != '*'):
                            break
                        I -= 1    
                    J = j+1
                    I = i
                    while (J < 8):
                        tabuleiro2[I][J] = switch2(tabuleiro2[I][J])
                        if(tabuleiro2[I][J] != '.' and tabuleiro2[I][J] != '*'):
                            break
                        J += 1
                    J = j-1
                    I = i
                    while (J >= 0):
                        tabuleiro2[I][J] = switch2(tabuleiro2[I][J])
                        if(tabuleiro2[I][J] != '.' and tabuleiro2[I][J] != '*'):
                            break   
                        J -= 1
            elif(tabuleiro[i][j] == 'q'): #Movimentos Rainha
                    I = i+1
                    J = j+1
                    while (I < 8 and J < 8):
                        tabuleiro2[I][J] = switch2(tabuleiro2[I][J])
                        if(tabuleiro2[I][J] != '.' and tabuleiro2[I][J] != '*'):
                            break
                        I += 1    
                        J += 1
                    I = i+1
                    J = j-1
                    while (I < 8 and J >= 0):
                        tabuleiro2[I][J] = switch2(tabuleiro2[I][J])
                        if(tabuleiro2[I][J] != '.' and tabuleiro2[I][J] != '*'):
                            break
                        I += 1    
                        J -= 1
                    I = i-1
                    J = j+1
                    while (I >= 0 and J < 8):
                        tabuleiro2[I][J] = switch2(tabuleiro2[I][J])
                        if(tabuleiro2[I][J] != '.' and tabuleiro[I][J] != '*'):
                            break
                        I -= 1    
                        J += 1
                    I = i-1
                    J = j-1
                    while (I >= 0 and J >= 0):
                        tabuleiro2[I][J] = switch2(tabuleiro2[I][J])
                        if(tabuleiro2[I][J] != '.' and tabuleiro2[I][J] != '*'):
                            break
                        I -= 1    
                        J -= 1
                    I = i+1
                    J = j
                    while (I < 8):
                        tabuleiro2[I][J] = switch2(tabuleiro2[I][J])
                        if(tabuleiro2[I][J] != '.' and tabuleiro2[I][J] != '*'):
                            break
                        I += 1    
                    I = i-1
                    J = j
                    while (I >= 0):
                        tabuleiro2[I][J] = switch2(tabuleiro2[I][J])
                        if(tabuleiro2[I][J] != '.' and tabuleiro2[I][J] != '*'):
                            break
                        I -= 1    
                    J = j+1
                    I = i
                    while (J < 8):
                        tabuleiro2[I][J] = switch2(tabuleiro2[I][J])
                        if(tabuleiro2[I][J] != '.' and tabuleiro2[I][J] != '*'):
                            break
                        J += 1
                    J = j-1
                    I = i
                    while (J >= 0):
                        tabuleiro2[I][J] = switch2(tabuleiro2[I][J])
                        if(tabuleiro2[I][J] != '.' and tabuleiro2[I][J] != '*'):
                            break   
                        J -= 1  


    #Verificação se o rei branco esta em xeque    
    if(tabuleiro2[casa_K[0]][casa_K[1]] == '*'):         
        jogos += 1
        print(f"Jogo #{jogos}: O rei branco esta em xeque")
        continue
    
    #Se nenhum dor estiver em cheque
    print(f"Jogo #{jogos}: Nenhum dos reis esta em xeque")
    jogos += 1
