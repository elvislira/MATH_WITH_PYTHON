from numpy import matrix
from numpy import zeros
from numpy import ones
from numpy import identity


# Matriz 3x3
A = matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
# Matriz 3x2
B = matrix([
    [9, 8],
    [7, 6],
    [5, 4]
])
print(f'A({A.shape}) -> {type(A)}')
print(f'B({B.shape}) -> {type(B)}')

# Matriz zero
C = zeros((2, 3), dtype='int')
print(f'Matriz zero\n{C}')

# Matriz um
D = ones((2, 3), dtype='int')
print(f'Matriz um\n{D}')

# Matriz identidade
E = identity(3, dtype='int')
print(f'Matriz identidade\n{E}')
