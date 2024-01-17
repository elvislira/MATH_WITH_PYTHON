from pylab import plot
from pylab import show
from pylab import arange
from pylab import subplot
from pylab import title


# Função a ser plotada no gráfico 1
def f(x):
    return 2 * x

# Função a ser plotada no gráfico 2
def g(x):
    return x ** 2

x = arange(-3, 3, 0.3)
y1 = f(x)
y2 = g(x)

subplot(121)
plot(x, y1, 'mo')
title('Gráfico 1')

subplot(122)
plot(x, y2, 'g^')
title('Gráfico 2')

show()
