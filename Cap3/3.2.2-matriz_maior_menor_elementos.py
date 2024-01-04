from numpy import matrix


A = matrix([
    [7, 2, 4],
    [3, 5, 9]
])

print(f'Matriz\n{A}')

print(f'Maior valor da matriz: {A.max()}')
print(f'Maior valor por coluna: {A.max(axis=0)}')
print(f'Maior valor por linha: {A.max(axis=1)}')

print(f'Menor valor da matriz: {A.min()}')
print(f'Menor valor por coluna: {A.min(axis=0)}')
print(f'Menor valor por linha: {A.min(axis=1)}')
