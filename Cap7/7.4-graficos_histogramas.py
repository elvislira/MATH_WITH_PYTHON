from numpy.random import randn
from numpy.random import seed
from pylab import hist
from pylab import show
from pylab import xlabel
from pylab import ylabel
from pylab import title
from pylab import axis

seed(200)
media = 10
desvio_padrao = 3

valores_gerados = media + desvio_padrao * randn(3000)

xlabel('Valores')
ylabel('Probabilidade')
title('Histograma')

hist(
    x=valores_gerados, 
    bins=30, 
    color='b'
)

show()
