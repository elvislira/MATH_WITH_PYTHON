from sympy import Derivative
from sympy import Symbol
from sympy import N


# Função a ser retornado
def f(x):
    return 1/x

x = Symbol('x')


derivada = Derivative(f(x), x).doit()
resultado_x_3 = derivada.subs({x:3})

print(f'Derivada de {f(x)} = {derivada}')
print(f'Para x = 3 é: {resultado_x_3} ou {N(resultado_x_3)}')
