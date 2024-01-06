from numpy import matrix


X = matrix([
    [7, 2, 4],
    [3, 5, 9]
])

Y = matrix([
    [3, 6, 9],
    [1, 8, 2]
])

print(f'Matriz X\n{X}')
print(f'Matriz Y\n{Y}')

# Soma das matrizes X e Y
Z = X + Y
print(f'Soma das matrizes X e Y\z{Z}')

# Subtração das matrizes X e Y
Z = X - Y
print(f'Subtração das matrizes X e Y\z{Z}')
