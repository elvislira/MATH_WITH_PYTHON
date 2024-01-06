from numpy import matrix
from numpy import linalg


A = matrix([
    [7, 2, 4],
    [3, 5, 9],
    [1, 6, 8]
])

detA = linalg.det(A)
print(f'detA = {detA}')
