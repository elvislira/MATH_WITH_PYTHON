from numpy import matrix
from numpy import power
from numpy import multiply


X = matrix([
    [7, 2, 4],
    [3, 5, 9],
    [1, 6, 8]
])

Y = matrix([
    [3, 6, 9],
    [1, 8, 2],
    [7, 2, 4]
])

print(f'Matriz X\n{X}')
print(f'Matriz Y\n{Y}')

# Cria uma matriz B, a partir de X, onde cada
# elemento de A será acrescido de 5 unidades
B = X + 5
print(f'Matriz B\n{B}')

# Cria uma matriz C, a partir de X, onde cada
# elemento de A será subtraído de 5 unidades
C = X - 5
print(f'Matriz C\n{C}')

# Cria uma matriz D, a partir de X, onde cada
# elemento de A será multiplicado por 5
D = X * 5
print(f'Matriz D\n{D}')

# Cria uma matriz E, a partir de X, onde cada
# elemento de A será dividido por 2
E = X / 2
print(f'Matriz E\n{E}')

# Cria uma matriz F, a partir de X, onde cada
# elemento de A será elevado a 3
F = power(X, 3)
print(f'Matriz F\n{F}')

# Cria uma matriz G, a partir de X, onde cada
# elemento de X será multiplicado por cada elemento de Y
G = multiply(X, Y)
print(f'Matriz G\n{G}')

# Cria uma matriz H, a partir de X, onde cada
# elemento de X será dividido por cada elemento de Y
H = X / Y
print(f'Matriz H\n{H}')