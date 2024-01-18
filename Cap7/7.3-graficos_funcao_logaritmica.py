from pylab import log
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
    return log(x)

x = arange(1, 9, 0.1)
y = f(x)

plot(x, y, 'b')

xlabel('Eixo x')
ylabel('Eixo y ou f(x)')
title('Função Exponencial: log(x)')

grid()

axhline(y=0, color='k')

axis([1, 9, 0, 2.5])

show()
