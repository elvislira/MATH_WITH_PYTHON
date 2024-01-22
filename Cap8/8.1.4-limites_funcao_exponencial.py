from sympy import Limit
from sympy import Symbol
from sympy import S
from math import exp


# Função a ser retornada
def f(x):
    return (1 + (1/x)) ** (2*x)

x = Symbol('x')

# Cálculo dos limites
lim_x_tende_0 = Limit(f(x), x, 0).doit()
lim_x_tende_infinito = Limit(f(x), x, S.Infinity).doit()
lim_x_tende_menos_infinito = Limit(f(x), x, -S.Infinity).doit()

# Exibição dos resultados
print(f'lim({f(x)}), x->0 = {lim_x_tende_0}')
print(f'lim({f(x)}), x->{S.Infinity} = {lim_x_tende_infinito} = {eval(str(lim_x_tende_infinito))}')
print(f'lim({f(x)}), x->-{S.Infinity} = {lim_x_tende_menos_infinito} = {eval(str(lim_x_tende_menos_infinito))}')
