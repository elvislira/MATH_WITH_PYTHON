# Função a ser retornada
def f(x):
    return x**3 + 5*x**2 - 5*x - 12

iteracao = 0
iteracao_maxima = 100

erro_definido = 0.0001

parar = 0

# Limites inferior(a) e superior(b)
a = -6.0
b = -4.0

y1 = f(a)
y2 = f(b)

c_anterior = 2 * b

if y1*y2 > 0:
    print('Erro de execução - redefinir valores de a e b')
else:
    while parar == 0:
        iteracao += 1
        c = b - (y2 * (b-a)) / (y2-y1)
        yc = f(c)
        
        if y1*yc > 0:
            a = c
            
        if y2*yc > 0:
            b = c
            
        erro = abs(c - c_anterior)
        c_anterior = c
        
        if iteracao > iteracao_maxima or erro < erro_definido:
            parar = 1
        
    print(f'Total de iterações: {iteracao}')
    print(f'Valor de x: x={c}')
    print(f'Erro encontrado: erro={erro}')
