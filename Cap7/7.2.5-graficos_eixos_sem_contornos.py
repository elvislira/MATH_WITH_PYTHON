from pylab import subplots
from pylab import arange
from pylab import show
from pylab import xlabel
from pylab import ylabel
from pylab import title

# Retorna a função a ser plotada no gráfico
def f(x):
    return 2 * x

x = arange(-4, 4, 0.5)
y = f(x)

fig, ax = subplots()

ax.plot(x, y)
ax.grid(True, which='both')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

xlabel(
    'Eixo das bscissas (X)', 
    horizontalalignment='right', 
    position=(1, 10))
ylabel(
    'Eixo das ordenadas (Y)', 
    verticalalignment='top', 
    position=(1, 0.7))
title('Função do Primeiro Grau')

show()
