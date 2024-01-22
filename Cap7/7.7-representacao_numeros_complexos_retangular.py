from pylab import show
from pylab import plot
from pylab import text
from pylab import axis
from pylab import axhline
from pylab import axvline
from pylab import grid
from pylab import title


z = 5 + 3j
w = 2 - 4j

# Representação retangular
plot([0, z.real], [0, z.imag], 'ro-')
text(z.real+0.2, z.imag+0.2, f'{z}')
plot([0, w.real], [0, w.imag], 'b*--')
text(w.real+0.2, w.imag+0.2, f'{w}')

title('Números complexos - Forma retangular')

axis([0, 7, -5, 4])

axhline(y=0, color='k')
axvline(x=0, color='k')

grid()

show()
