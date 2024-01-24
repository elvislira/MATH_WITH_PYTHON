from sympy import Derivative
from sympy import Symbol
from sympy import exp
from sympy import sin
from sympy import N


# Função a ser retornada
def f(x):
    return x * exp(x)

def g(x):
    return exp(3*x) * sin(x/3)

x = Symbol('x')

# Derivadas de f(x)
derivada_fx_ordem_1 = Derivative(f(x), x).doit()
derivada_fx_ordem_2 = Derivative(f(x), x, 2).doit()
derivada_fx_ordem_3 = Derivative(f(x), x, 3).doit()

print(f'Derivadas {f(x)}:')
print(f'\tPrimeira ordem = {derivada_fx_ordem_1}')
print(f'\tSegunda ordem = {derivada_fx_ordem_2}')
print(f'\tTerceira ordem = {derivada_fx_ordem_3}')

# Derivadas de g(x)
derivada_gx_ordem_1 = Derivative(g(x), x).doit()
derivada_gx_ordem_2 = Derivative(g(x), x, 2).doit()
derivada_gx_ordem_3 = Derivative(g(x), x, 3).doit()

print(f'\nDerivadas {g(x)}:')
print(f'\tPrimeira ordem = {derivada_gx_ordem_1}')
print(f'\tSegunda ordem = {derivada_gx_ordem_2}')
print(f'\tTerceira ordem = {derivada_gx_ordem_3}')
