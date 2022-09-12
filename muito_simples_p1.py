def distancia(p1,p2:list) -> float:
    '''A função distancia calcula a distancia entre dois pontos, considerando-se que os
    pontos são duas listas com dois valores cada, e imprime distancia como um valor float.
    A função funciona apenas para o plano cartesiano
    '''
    dist = (((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))**(0.5)
    print("{:.5f}".format(dist))
        