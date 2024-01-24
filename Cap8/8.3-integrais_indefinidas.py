from sympy import Integral
from sympy import Symbol


# Função a ser retornada
def f(x):
    return -1/x**2

x = Symbol('x')

primitiva = Integral(f(x), x).doit()

print(f'Integral indefinida de {f(x)} = {primitiva}')
