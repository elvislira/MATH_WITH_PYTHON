# Função desenvolvida para extração de qualquer raiz (quadrada, cúbica, etc...)
def raiz_enesima(radicando: float, indice: float) -> float:
    if indice <= 0:
        return None
    
    return radicando ** (1/indice)

radicando = 1024
indice = -2.1

print(f'{raiz_enesima(radicando, indice)}')
