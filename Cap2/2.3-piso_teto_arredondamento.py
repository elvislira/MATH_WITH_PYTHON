import math as mt
import numpy as np


x = 3.5615

v1 = mt.ceil(x)
v2 = mt.floor(x)

print('\n--- MATH ---')
print(f'ceil - {v1}({type(v1)})')
print(f'floor - {v2}({type(v2)})')

v1 = np.ceil(x)
v2 = np.floor(x)

print('\n--- NUMPY ---')
print(f'ceil - {v1}({type(v1)})')
print(f'floor - {v2}({type(v2)})')

v3 = round(x)
v4 = round(x, 3)

print('\n--- ARREDONDAMENTO ---')
print(f'round - {v3}({type(v3)})')
print(f'round - {v4}({type(v4)})')

