from sympy import Limit
from sympy import Symbol
from sympy import S
from sympy import sin
from math import pi


# Função a ser retornada
def f(x):
    return sin(2*x) / x

x = Symbol('x')

# Cálculo dos limites
lim_x_tende_0 = Limit(f(x), x, 0).doit()
lim_x_tende_pi_sobre_6 = Limit(f(x), x, pi/6).doit()
lim_x_tende_infinito = Limit(f(x), x, S.Infinity).doit()
lim_x_tende_menos_infinito = Limit(f(x), x, -S.Infinity).doit()

# Exibição dos resultados
print(f'lim({f(x)}), x->0 = {lim_x_tende_0}')
print(f'lim({f(x)}), x->pi/6 = {lim_x_tende_pi_sobre_6}')
print(f'lim({f(x)}), x->{S.Infinity} = {lim_x_tende_infinito}')
print(f'lim({f(x)}), x->-{S.Infinity} = {lim_x_tende_menos_infinito}')
