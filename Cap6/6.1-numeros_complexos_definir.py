from cmath import exp
from cmath import pi


# Forma retangular
z = 5 + 3j
# Forma exponencial
w = 5 * exp(1j * pi/6)

print(f'Forma retangular: {z:.1f}')
# Mesmo definindo o número na forma exponencial
# a exibição será na forma retuangular
print(f'Forma retangular: {w:.1f}')