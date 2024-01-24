from sympy import Derivative
from sympy import Symbol


# Função a ser retornada
def f(x):
    return x**3 + 2*x**2

x = Symbol('x')

derivada_ordem_1 = Derivative(f(x), x).doit()
derivada_ordem_2 = Derivative(f(x), x, 2).doit()
derivada_ordem_3 = Derivative(f(x), x, 3).doit()

print(f'Derivada de {f(x)} = {derivada_ordem_1}')
print(f'Derivada de 2ª ordem de {f(x)} = {derivada_ordem_2}')
print(f'Derivada de 3ª ordem de {f(x)} = {derivada_ordem_3}')
