from sympy import Integral
from sympy import Symbol
from sympy import exp
from sympy import sin


# Função a ser retornada
def f(x):
    return 3 * exp(3*x) * sin(x/2)

x = Symbol('x')

primitiva = Integral(f(x), x).doit()

print(f'Integral definida de {f(x)} = {primitiva}')
