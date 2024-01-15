from cmath import polar
from cmath import phase
from cmath import exp
from cmath import pi
from math import degrees
from numpy import conj


# Forma retangular
z = 4 + 3j

print(f'Número complexo: z = 5 + 3j')
print(f'Forma retangular: {z}')
print(f'Conjugado de z: {conj(z)}')
print(f'Parte real de z: {z.real}')
print(f'Parte imaginária de z: {z.imag}')
print(f'Forma polar: {polar(z)}')
print(f'Módulo de z: {abs(z)}')
print(f'Agumento, em radianos, de z: {phase(z)}')
print(f'Agumento, em graus, de z: {degrees(phase(z))}\n\n')


# Forma exponencial
w = 5 * exp(1j * pi/6)

print(f'Número complexo: w = 5 * exp(1j * pi/6)')
print(f'Forma retangular: {w}')
print(f'Conjugado de w: {conj(w)}')
print(f'Parte real de w: {w.real}')
print(f'Parte imaginária de w: {w.imag}')
print(f'Forma polar: {polar(w)}')
print(f'Módulo de w: {abs(w)}')
print(f'Agumento, em radianos, de w: {phase(w)}')
print(f'Agumento, em graus, de w: {degrees(phase(w))}')
