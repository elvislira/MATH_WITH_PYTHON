from math import sin
from math import cos
from math import tan
from math import pi
from math import radians, degrees


def tabela_trigonometrica(titulo):
    print(f'\n=== {titulo} ===')
    print(f'  \t30°\t45°\t60°')
    print(f'sen\t{s30:.3f}\t{s45:.3f}\t{s60:.3f}')
    print(f'cos\t{c30:.3f}\t{c45:.3f}\t{c60:.3f}')
    print(f'tg\t{t30:.3f}\t{t45:.3f}\t{t60:.3f}')

# Em Radianos
# 30°
s30 = sin(pi/6)
c30 = sin(pi/6)
t30 = tan(pi/6)
# 45°
s45 = sin(pi/4)
c45 = sin(pi/4)
t45 = tan(pi/4)
# 60°
s60 = sin(pi/3)
c60 = sin(pi/3)
t60 = tan(pi/3)

tabela_trigonometrica('Usando ângulo em Radianos')

# Em Graus
# 30°
s30 = sin(radians(30))
c30 = sin(radians(30))
t30 = tan(radians(30))
# 45°
s45 = sin(radians(45))
c45 = sin(radians(45))
t45 = tan(radians(45))
# 60°
s60 = sin(radians(60))
c60 = sin(radians(60))
t60 = tan(radians(60))

tabela_trigonometrica('Usando ângulo em Graus')
