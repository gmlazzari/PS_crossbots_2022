def converte_temperatura(F:float) -> float:
    '''
    A função recebe uma temperatura em Fahrenheit do tipo float
    e imprime a temperatura em Celsius, tambem do tipo  float.
    '''
    C = 5*(F-32)/9
    print("{:.2f}".format(C))
    
