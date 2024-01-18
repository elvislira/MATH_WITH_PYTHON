from pylab import sin
from pylab import cos
from pylab import tan
from pylab import pi
from pylab import plot
from pylab import subplot
from pylab import show
from pylab import arange
from pylab import xlabel
from pylab import ylabel
from pylab import title
from pylab import grid
from pylab import axhline
from pylab import axis


# Funções a serem retornadas
def f(x):
    return sin(x)

def g(x):
    return cos(x)

def h(x):
    return tan(x)

x = arange(0.0, 3*pi, 0.01)
y1 = f(x)
y2 = g(x)
y3 = h(x)

subplot(311)
plot(x, y1, 'm')
title('Seno de x')
xlabel('Eixo x')
ylabel('Eixo y ou f(x)')
grid()
axhline(y=0, color='k')
axis([0, 10, -1.1, 1.1])

subplot(312)
plot(x, y2, 'g')
title('Coseno de x')
xlabel('Eixo x')
ylabel('Eixo y ou f(x)')
grid()
axhline(y=0, color='k')
axis([0, 10, -1.1, 1.1])

subplot(313)
plot(x, y3, 'b')
title('Tangente de x')
xlabel('Eixo x')
ylabel('Eixo y ou f(x)')
grid()
axhline(y=0, color='k')
axis([0, 10, -20, 20])

show()
