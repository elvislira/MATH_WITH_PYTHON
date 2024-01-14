from sympy import Symbol
from sympy import solve
from sympy import log


x = Symbol('x')

# Retorna a função log4(3x + 2) - log4(2x + 5)
def f(x):
    return log((3*x+2)/(2*x+5), 4)

y = f(x)
solucao = solve(y)
print(f'log4(3x + 2) - log4(2x + 5) = 0, S={solucao}')

# Retorna a função logx(2x + 3) - 2
def g(x):
    return log(2*x+3, x) - 2

y = g(x)
solucao = solve(y)
print(f'logx(2x + 3) - 2 = 0, S={solucao}')

# Retorna a função x^(logx(x+3)) - 7
def h(x):
    return x**(log(x+3, x)) - 7

y = h(x)
solucao = solve(y)
print(f'x^(logx(x+3)) - 7 = 0, S={solucao}')
