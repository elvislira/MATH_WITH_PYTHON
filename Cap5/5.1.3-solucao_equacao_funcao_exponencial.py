from sympy import Symbol
from sympy import solve
from sympy import exp


# Define x como variável
x = Symbol('x')

# Retorna a função 2^x - 8
def f(x):
    return 2**x - 8

y = f(x)
solucao = solve(y)
print(f'2^x - 8 = 0, S={solucao}')

# Retorna a função e^(2*x + 1) - e^(3*x - 4)
def g(x):
    return exp(2*x + 1) - exp(3*x - 4)

y = g(x)
solucao = solve(y)
print(f'e^(2*x + 1) - e^(3*x - 4) = 0, S{solucao}')

# Retorna a função x^(x²-7x-18) - 1
def h(x):
    return x**(x**2 - 7*x - 18) - 1

y = h(x)
solucao = solve(y)
print(f'x^(x²-7x-18) - 1 = 0, S={solucao}')
