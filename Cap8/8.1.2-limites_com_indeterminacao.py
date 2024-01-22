from sympy import Limit
from sympy import Symbol
from sympy import S


# Função a ser retornada
def f(x):
    return (x**3 - 1) / (x - 1)

x = Symbol('x')

# Cálculo dos limites
lim_x_tende_1 = Limit(f(x), x, 1).doit()
lim_x_tende_infinito = Limit(f(x), x, S.Infinity).doit()
lim_x_tende_menos_infinito = Limit(f(x), x, -S.Infinity).doit()
lim_x_tende_1_direita = Limit(f(x), x, 1, '+').doit()
lim_x_tende_1_esquerda = Limit(f(x), x, 1, '-').doit()

# Exibição dos resultados
print(f'lim({f(x)}), x->1 = {lim_x_tende_1}')
print(f'lim({f(x)}), x->{S.Infinity} = {lim_x_tende_infinito}')
print(f'lim({f(x)}), x->-{S.Infinity} = {lim_x_tende_menos_infinito}')
print(f'lim({f(x)}), x->1+ = {lim_x_tende_1_direita}')
print(f'lim({f(x)}), x->1- = {lim_x_tende_1_esquerda}')
