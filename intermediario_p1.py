import math

def angulo_3pontos(pA,pB,pC:list) ->float:
    '''
    Essa função recebe tres pontos do plano cartesiano em formato de lista
    e imprime o angulo entre os pontos em radianos'''
    v_AB = [pB[0]-pA[0],pB[1]-pA[1]]
    v_CB = [pB[0]-pC[0],pB[1]-pC[1]]
    norma_vAB = ((v_AB[0]**2)+(v_AB[1]**2))**(0.5)
    norma_vCB = ((v_CB[0]**2)+(v_CB[1]**2))**(0.5)
    ang = math.acos((v_AB[0]*v_CB[0]+v_AB[1]*v_CB[1])/(norma_vAB*norma_vCB))
    
    print("{:.4f}".format(ang))
    