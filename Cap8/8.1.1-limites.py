from sympy import Limit
from sympy import Symbol
from sympy import S


# Função a ser retornada
def f(x):
    return 1/x

x = Symbol('x')

# Cálculo dos limites
lim_x_tende_3 = Limit(f(x), x, 3).doit()
lim_x_tende_infinito = Limit(f(x), x, S.Infinity).doit()
lim_x_tende_menos_infinito = Limit(f(x), x, -S.Infinity).doit()
lim_x_tende_zero_direita = Limit(f(x), x, 0, '+').doit()
lim_x_tende_zero_esquerda = Limit(f(x), x, 0, '-').doit()

# Exibição dos resultados
print(f'lim({f(x)}), x->3 = {lim_x_tende_3}')
print(f'lim({f(x)}), x->{S.Infinity} = {lim_x_tende_infinito}')
print(f'lim({f(x)}), x->-{S.Infinity} = {lim_x_tende_menos_infinito}')
print(f'lim({f(x)}), x->0+ = {lim_x_tende_zero_direita}')
print(f'lim({f(x)}), x->0- = {lim_x_tende_zero_esquerda}')
