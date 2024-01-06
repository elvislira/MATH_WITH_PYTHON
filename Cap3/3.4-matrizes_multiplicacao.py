from numpy import matrix


X = matrix([
    [7, 2, 4],
    [3, 5, 9]
])

Y = matrix([
    [3, 9],
    [5, 8],
    [7, 6]
])

print(f'Matriz X\n{X}')
print(f'Matriz Y\n{Y}')

# Multiplicação da matriz X pela matriz Y
Z = X * Y
print(f'Multiplicação da matriz X pela matriz Y\z{Z}')
