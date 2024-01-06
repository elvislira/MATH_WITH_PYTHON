from numpy import matrix


A = matrix([
    [7, 2, 4],
    [3, 5, 9],
    [5, 3, 6]
])

soma_elementos = A.sum()
print(f'Soma dos elementos: {soma_elementos}')
soma_elementos_colunas = A.sum(axis=0)
print(f'Soma dos elementos das colunas: {soma_elementos_colunas}')
soma_elementos_linhas = A.sum(axis=1)
print(f'Soma dos elementos das linhas: {soma_elementos_linhas}')
