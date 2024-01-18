from pylab import plot
from pylab import show
from pylab import arange
from pylab import axhline
from pylab import grid
from pylab import axis
from pylab import xlabel
from pylab import ylabel
from pylab import title


# Função a ser retornada
def f(x):
    return 2 ** x

x = arange(-5, 5, 0.1)
y = f(x)

plot(x, y, 'g')

xlabel('Eixo x')
ylabel('Eixo y ou f(x)')
title('Função Exponencial: 2^x')

grid()

axhline(y=0, color='k')

axis([-5, 2, 0, 3])

show()
