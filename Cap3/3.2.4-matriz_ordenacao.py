from numpy import matrix


A = matrix([
    [7, 2, 4],
    [3, 5, 9],
    [1, 6, 8]
])

indice = A[:, 0].argsort(axis=0)
B = A[indice, :]
print(f'MAtriz ordenada crescente primeira coluna: {B}')
