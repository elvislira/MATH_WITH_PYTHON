from math import e #constante de Euler


# Calcula a elevado a x
# dada a condições: 0 < a # 1
def exponencial(a: float, x: float) -> float:
    if a == 1 or a <= 0:
        return None
    
    return a ** x

if __name__ == '__main__':
    a = 3
    x = 2

    base_qualquer = exponencial(a, x)
    base_e = exponencial(e, x) # É o mesmo que exp(x)

    print(f'{e} elvado a {x} é igual a {base_e:.3f}')
    
    if base_qualquer != None:
        print(f'{a} elvado a {x} é igual a {base_qualquer:.3f}')
    else:
        print('Verifique as condições de existência.')

    