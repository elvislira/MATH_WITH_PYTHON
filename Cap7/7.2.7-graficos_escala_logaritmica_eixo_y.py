from pylab import plot
from pylab import show
from pylab import arange
from pylab import yscale


# Função a ser plotada
def f(x):
    return x ** 8

x = arange(0, 4, 0.1)
y = f(x)

plot(x, y)

yscale('log')

show()
