from pylab import plot
from pylab import arange
from pylab import show

# Define as funções a serem plotadas
def f(x):
    return 2 * x

def g(x):
    return 3 * f(x)

def h(x):
    return x ** 2

x = arange(0, 4, 0.5)
y1 = f(x)
y2 = g(x)
y3 = h(x)

plot(x, y1, x, y2, x, y3)

show()
