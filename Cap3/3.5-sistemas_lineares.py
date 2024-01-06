from numpy import matrix
from numpy import linalg


# Resolução do seguinte sistema:
#                      A        X       B
# |2x - 5y = 11     |2  -5|    |x|     |11|
# |3x + 6y = 3      |3   6|    |y|     |3 |
# Lembrando que: X = A⁻¹ x B = X

A = matrix([
    [2, -5],
    [3, 6]
])

B = matrix([
    [11],
    [3]
])

X = linalg.inv(A) * B

print('''
Solução do sistema:
    |2x - 5y = 11
    |3x + 6y = 3 
''')
print(f'{X}\n')

# Resolução do seguinte sistema:
#                           A        X       B
# |3x - y + z = 11        |3  -1  1|    |x|     | 11|
# |-2x + 3y -3z = -19      |-2  3 -3|    |y|     | 19|
# |-x - 3y -4z = -15      |-1 -3 -4|    |y|     |-15|
# Lembrando que: X = A⁻¹ x B = X

A = matrix([
    [3, -1, 1],
    [-2, 3, -3],
    [-1, -3, -4]
])

B = matrix([
    [11],
    [-19],
    [-15]
])

X = linalg.inv(A) * B

print('''
Solução do sistema:
    |3x - y + z = 11
    |-2x + 3y -3z = -19
    |-x - 3y -4z = -15
''')
print(f'{X}\n')

