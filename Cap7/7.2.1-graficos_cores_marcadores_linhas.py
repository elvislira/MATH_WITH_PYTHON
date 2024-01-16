from pylab import plot
from pylab import show
from pylab import arange


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

plot(x, y1, 'co:')
plot(x, y2, 'k^--')
plot(x, y3, 'g*')

show()
