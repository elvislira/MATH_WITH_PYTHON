from numpy import matrix
from numpy import transpose
from numpy import linalg

# Matriz transposta
A = matrix([
    [7, 2, 4],
    [3, 5, 9]
])
print(f'Matriz A\n{A}')
print(f'Matriz transposta de A\n{transpose(A)}')

# Matriz inversa
B = matrix([
    [7, 2, 4],
    [3, 5, 9],
    [1, 6, 8]
])
print(f'Matriz B\n{B}')
print(f'Matriz inversa\n{linalg.inv(B)}')
