from sympy import Derivative
from sympy import Symbol


# Função a ser retornada
def f(x):
    return x**3 + 5*x**2 - 5*x - 12

x = Symbol('x')

iteracao = 0
iteracao_maxima = 100

erro_definido = 0.0001

parar = 0

x0 = -5.0

while parar == 0:
    iteracao += 1
    
    f_x0 = f(x0)
    
    d = Derivative(f(x), x)
    
    f_linha_x0 = d.doit().subs({x: x0})
    
    x1 = x0 - (f_x0 / f_linha_x0)
    
    erro = abs(x0 - x1)
    
    x0 = x1
    
    if iteracao > iteracao_maxima or erro < erro_definido:
        parar = 1
        
print(f'Total de iterações: {iteracao}')
print(f'Valor de x: x={x0}')
print(f'Erro encontrado: erro={erro}')