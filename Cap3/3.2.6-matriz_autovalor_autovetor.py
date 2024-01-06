from numpy import matrix
from numpy import linalg


A = matrix([
    [1, 0, 0],
    [0, 2, 0],
    [0, 0, 3]
])

resultado = linalg.eig(A)

print(f'{resultado}\n')
print(f'Autovalores de A\n{resultado[0]}')
print(f'Autovetores de A\n{resultado[1]}')
