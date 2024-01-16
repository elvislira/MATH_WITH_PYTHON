from pylab import plot
from pylab import show
from pylab import arange
from pylab import xlabel
from pylab import ylabel
from pylab import title
from pylab import grid
from pylab import axhline
from pylab import axvline
from pylab import annotate


# Define a função a ser retornada
def f(x):
    return 5 * x

x = arange(0, 4, 0.5)
y = f(x)

plot(x, y, 'o')

xlabel('Eixo das bscissas (X)')
ylabel('Eixo das ordenadas (Y)')
title('Função do Primeiro Grau')

axhline(y=0, color='b')
axvline(x=0, color='b')

grid(True)

annotate(
    'A(1.5, 7.5)',
    xy=(1.5, f(1.5)),
    xytext=(1.8, 5),
    arrowprops=dict(
        facecolor='k', 
        shrink=0.1
    )
)

annotate(
    'B(2.5, 12.5)',
    xy=(2.5, f(2.5)),
    xytext=(1.5, 14.5),
    arrowprops=dict(
        facecolor='k', 
        shrink=0.1
    )
)

show()
