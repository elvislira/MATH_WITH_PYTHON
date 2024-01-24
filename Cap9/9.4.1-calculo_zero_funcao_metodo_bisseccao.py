# Função a ser retornada
def f(x):
    return x**3 + 5*x**2 - 5*x - 12

iteracao = 0
iteracao_maxima = 100

erro_definido = 0.0001

parar = 0

# Limites inferior(a) e superior(b)
a = -2.0
b = 1.0

y1 = f(a)
y2 = f(b)

x0_anterior = 2 * b

if y1*y2 > 0:
    print('Erro de execução - redefinir valores de a e b')
else:
    while parar == 0:
        iteracao += 1
        x0 = (a + b) / 2
        y0 = f(x0)
        
        if y1*y0 > 0:
            a = x0
            
        if y2*y0 > 0:
            b = x0
            
        erro = abs(x0 - x0_anterior)
        x0_anterior = x0
        
        if iteracao > iteracao_maxima or erro < erro_definido:
            parar = 1
        
    print(f'Total de iterações: {iteracao}')
    print(f'Valor de x: x={x0}')
    print(f'Erro encontrado: erro={erro}')
