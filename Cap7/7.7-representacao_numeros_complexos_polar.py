from pylab import polar
from pylab import show
from pylab import angle
from pylab import title


z = 5 + 3j
w = 2 - 4j

angulo_z = [0, angle(z)]
angulo_w = [0, angle(w)]
modulo_z = [0, abs(z)]
modulo_w = [0, abs(w)]

# Representação polar
polar(angulo_z, modulo_z, marker='*')
polar(angulo_w, modulo_w, marker='o')

title('Números complexos - Forma polar')

show()
