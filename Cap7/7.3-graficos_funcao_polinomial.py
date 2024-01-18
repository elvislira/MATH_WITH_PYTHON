from pylab import plot
from pylab import arange
from pylab import show
from pylab import xlabel
from pylab import ylabel
from pylab import title
from pylab import grid
from pylab import axhline
from pylab import axvline
from pylab import axis


# Função a ser plotada
def f(x):
    return -x**2 - 2*x + 15

x = arange(-10, 8, 0.1)
y = f(x)

plot(x, y)

xlabel('Eixo x')
ylabel('Eixo y ou f(x)')
title('Função Quadrática: -x² - 2x + 15')

grid(True)

axhline(y=0, color='k')
axvline(x=0, color='k')

axis([-10, 8, -70, 20])

show()
