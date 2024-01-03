from numpy.polynomial import Polynomial
from numpy import polyadd
from numpy import polysub
from numpy import polymul
from numpy import polydiv
from copy import deepcopy

# Operações com polinômios

# Polinômios
p1 = Polynomial([-1, 2, 3]) #3x² + 2x - 1
p2 = Polynomial([3, -1, 4]) #4x² - x + 3
p3_ = [4, 6, 3, 2]
p3 = Polynomial([2, 3, 6, 4]) #4x³ + 6x² + 3x + 2
p4 = Polynomial([2, 1, 2]) #2x² + x + 2

# Soma de polinômios 
soma = Polynomial(polyadd(p1, p2))
# print(f'({p1}) + ({p2}) = {soma}')

# Subtração de polinômios
subtracao = Polynomial(polysub(p1, p2))
# print(f'({p1}) - ({p2}) = {subtracao}')

# Multiplicação de polinômios
multiplicacao = Polynomial(polymul(p3, p4))
# print(f'({p3}) x ({p4}) = {multiplicacao}')

# Divisão de polinômios
aux = polydiv(p3_, list(p4))
a1 = list(aux[0])
a2 = list(aux[1])
print(f'{a1} | {type(a1)}')
print(f'{a2} | {type(a2)}')


quociente = Polynomial(a1)
resto = Polynomial(a2)
print(f'({p3}) / ({p4}) = {quociente}, Resto: {resto}')
