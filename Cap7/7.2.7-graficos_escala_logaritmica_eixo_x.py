from pylab import plot
from pylab import show
from pylab import arange
from pylab import xscale


# Função a ser plotada
def f(x):
    return x ** (1.0/8)

x = arange(0, 10000, 10)
y = f(x)

plot(x, y)

xscale('log')

show()
