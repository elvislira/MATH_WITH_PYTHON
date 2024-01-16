from pylab import plot
from pylab import show
from pylab import arange
from pylab import legend
from pylab import text
from pylab import xlabel
from pylab import ylabel
from pylab import title
from pylab import grid


# Define as funções a serem plotadas
def f(x):
    return 5*x - 1

def g(x):
    return x**2 + 2*x - 1

def h(x):
    return 2 ** x

x = arange(-4, 4, 0.2)
y1 = f(x)
y2 = g(x)
y3 = h(x)

plot(x, y1, 'co:', label='5x-1')
plot(x, y2, 'k^--', label='x²+2x-1')
plot(x, y3, 'g*', label='2^x')

legend(loc='lower right')
text(-4, 15, 'Minhas equações de primeiro grau,\nsegundo grau e exponencial')
xlabel('Eixo das bscissas (X)')
ylabel('Eixo das ordenadas (Y)')
title('Comparando Gráfico de Funções')

grid(True)

show()
