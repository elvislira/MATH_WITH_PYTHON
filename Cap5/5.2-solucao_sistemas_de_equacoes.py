from sympy import Symbol
from sympy import solve


# |-2x + 4y = 5
# | 3x - 2y = 3

x = Symbol('x')
y = Symbol('y')

def f(x, y):
    return -2*x + 4*y - 5

def g(x, y):
    return 3*x - 2*y - 3

z = f(x, y)
w = g(x, y)

solucao = solve((z, w))
print(f'|-2x + 4y = 5')
print(f'| 3x - 2y = 3')
print(f'S = {solucao}')

