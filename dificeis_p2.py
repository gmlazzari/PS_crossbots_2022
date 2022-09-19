def switch(c, cor = 'b'): #Funçao que marca o casas ocupadas pelas peças
    if(cor == 'b'):
        new_pos = "*" if c == '.' or c == 'k' else  c
    else:
        new_pos = "*" if c == '.' or c == 'K' else  c
    return new_pos

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


    for i in tabuleiro: #caso uma linha em branco entre na matriz
        if(len(i) == 0):
            tabuleiro.pop(i)
               
    def perc_tab(dir_i,dir_j,i,j,):
        '''
        Utilze o int 1 para direção positiva (para baixo e para direita),
        0  para constante (n se mexe naquela direção) e 
        -1 para negativo (para cima e para esquerda);
        E retorn uma lista com as posições que fora percorridas'''
    
        global tabuleiro
        list_pos_vazio = []
        i += (1*dir_i)
        j += (1*dir_j)
        while(i < 8 and i >= 0 and j < 8 and j >= 0):
            list_pos_vazio.append([i,j])
            if(tabuleiro[i][j] != '.' and tabuleiro[i][j] != '*'):
                break
            i += (1*dir_i)
            j += (1*dir_j)

        return list_pos_vazio 
    
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
    
    # Movimentos das Peças / espaços "ocupados" / Verificações   de xeque
    
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
                casas_occ = perc_tab(1,1,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]])
                casas_occ = perc_tab(1,-1,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]])
                casas_occ = perc_tab(-1,1,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]])
                casas_occ = perc_tab(-1,-1,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]]) 
            elif(tabuleiro[i][j] == 'N'): #Movimentos Cavalo
                vet_I = [-2,-2,-1,-1,1,1,2,2]
                vet_J = [1,-1,2,-2,2,-2,1,-1]
                for k in range(len(vet_I)):
                    I = i + vet_I[k]
                    J = j + vet_J[k]
                    if(I >= 0 and J >= 0):
                        try:
                            tabuleiro[I][J] = switch(tabuleiro[I][J])
                        except IndexError:
                            continue               
            elif(tabuleiro[i][j] == 'R'): #Movimentos Torre
                casas_occ = perc_tab(1,0,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]])
                casas_occ = perc_tab(-1,0,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]])
                casas_occ = perc_tab(0,1,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]])
                casas_occ = perc_tab(0,-1,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]])
            elif(tabuleiro[i][j] == 'Q'): #Movimentos Rainha
                casas_occ = perc_tab(1,1,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]])
                casas_occ = perc_tab(1,-1,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]])
                casas_occ = perc_tab(-1,1,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]])
                casas_occ = perc_tab(-1,-1,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]]) 
                casas_occ = perc_tab(1,0,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]])
                casas_occ = perc_tab(-1,0,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]])
                casas_occ = perc_tab(0,1,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]])
                casas_occ = perc_tab(0,-1,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]])

    #Verificação se o rei preto esta em xeque
    if(tabuleiro[casa_k[0]][casa_k[1]] == '*'):
        jogos += 1
        print(f"Jogo #{jogos}: O rei preto esta em xeque")
        continue
    
    for i in range(8): #Limpa os '*' das casas ocupadas pelas brancas
        for j in range(8):
            if(tabuleiro[i][j] == '*'):
                tabuleiro[i][j] = '.'

    #Espaços "ocupados" pelas peças pretas
    for i in range(8):
        for j in range(8):
            if(tabuleiro[i][j] == 'p'): #Movimentos Peão preto
                if(j == 0 and i != 0):
                    tabuleiro[i+1][j+1] = switch(tabuleiro[i+1][j+1],"p") 
                elif(j == 7 and i != 0):
                    tabuleiro[i+1][j-1] = switch(tabuleiro[i+1][j-1],"p")      
                elif(i != 0):
                    tabuleiro[i+1][j-1] = switch(tabuleiro[i+1][j-1],"p")
                    tabuleiro[i+1][j+1] = switch(tabuleiro[i+1][j+1],"p")                                             
            elif(tabuleiro[i][j] == 'b'): #Movimentos Bispo
                casas_occ = perc_tab(1,1,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]],"p")
                casas_occ = perc_tab(1,-1,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]],"p")
                casas_occ = perc_tab(-1,1,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]],"p")
                casas_occ = perc_tab(-1,-1,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]],"p") 
            elif(tabuleiro[i][j] == 'n'): #Movimentos Cavalo
                vet_I = [-2,-2,-1,-1,1,1,2,2]
                vet_J = [1,-1,2,-2,2,-2,1,-1]
                for k in range(len(vet_I)):
                    I = i + vet_I[k]
                    J = j + vet_J[k]
                    if(I >= 0 and J >= 0):
                        try:
                            tabuleiro[I][J] = switch(tabuleiro[I][J],"p")
                        except IndexError:
                            continue                   
            elif(tabuleiro[i][j] == 'r'): #Movimentos Torre
                casas_occ = perc_tab(1,0,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]],"p")
                casas_occ = perc_tab(-1,0,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]],"p")
                casas_occ = perc_tab(0,1,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]],"p")
                casas_occ = perc_tab(0,-1,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]],"p")
            elif(tabuleiro[i][j] == 'q'): #Movimentos Rainha
                casas_occ = perc_tab(1,1,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]],"p")
                casas_occ = perc_tab(1,-1,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]],"p")
                casas_occ = perc_tab(-1,1,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]],"p")
                casas_occ = perc_tab(-1,-1,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]],"p") 
                casas_occ = perc_tab(1,0,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]],"p")
                casas_occ = perc_tab(-1,0,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]],"p")
                casas_occ = perc_tab(0,1,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]],"P")
                casas_occ = perc_tab(0,-1,i,j)
                for k in casas_occ:
                    tabuleiro[k[0]][k[1]] = switch(tabuleiro[k[0]][k[1]],"P")  

    #Verificação se o rei branco esta em xeque    
    if(tabuleiro[casa_K[0]][casa_K[1]] == '*'):         
        jogos += 1
        print(f"Jogo #{jogos}: O rei branco esta em xeque")
        continue
    
    #Se nenhum dor estiver em cheque
    print(f"Jogo #{jogos}: Nenhum dos reis esta em xeque")
    jogos += 1

