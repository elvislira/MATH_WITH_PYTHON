from sympy import Symbol
from sympy import solve
from sympy import sin
from sympy import cos
from sympy import tan


# Define x como variável da equação
# Usado em todos os exemplos a seguir
x = Symbol('x')

# Retorna a função sen4x-1
def f(x):
    return sin(4 * x) - 1

y = f(x)
solucao = solve(y)
print(f'sen4x - 1 = 0, S{solucao}')

# Retorna a função 4cos²x - 3
def g(x):
    return 4 * (cos(x)**2) - 3

y = g(x)
solucao = solve(y)
print(f'4cos²x - 3 = 0, S={solucao}')

# Retorna a função sen²2x - cos2x - tan2x - 1
def h(x):
    return (sin(2*x)**2) - cos(2*x) - tan(2*x) - 1

y = h(x)
solucao = solve(y)
print(f'sen²2x - cos2x - tan2x - 1 = 0, S={solucao}')
