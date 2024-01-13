from sympy import Symbol
from sympy import solve

## Exemplo com função do Primeiro Grau
# Retorna a função a ser resolvida
def f(x):
    return 2*x + 1

# Define x como uma variável
x = Symbol('x') # será usado para todos os exemplos a seguir

# Calcula a equação (f(x)=0)
y = f(x)
solucao = solve(y)

print(f'2x+1=0, S={solucao}')

########################################
## Exemplo com função do Segundo Grau
def g(x):
    return x**2 - 4*x + 3

y = g(x)
solucao = solve(y)
print(f'x² - 4x + 3 = 0, S={solucao}')

########################################
## Exemplo com função do Segundo Grau com raízes não reais
def h(x):
    return x**2 + x + 1

y = h(x)
solucao = solve(y)
print(f'x² + x + 1 = 0, S{solucao}')

########################################
## Exemplo com função do Terceiro Grau
def k(x):
    return 3 * x**3 - 11 * x**2 + 5 * x + 3

y = k(x)
solucao = solve(y)
print(f'3x³ - 11x² + 5x + 3 = 0, S={solucao}')
