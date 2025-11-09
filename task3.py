import numpy as np

A = np.array([
    [-2.0, -8.5, -3.4, 3.5],
    [0.0,  2.4,  0.0, 8.2],
    [2.5,  1.6,  2.1, 3.0],
    [0.3, -0.4, -4.8, 4.6]
])

B = np.array([-1.88, -3.28, -0.5, -2.83])

A_revers = np.linalg.inv(A)

X = A_revers @ B

# ответ до одного знака после запятой
x1 = round(X[0], 1)
x2 = round(X[1], 1)
x3 = round(X[2], 1)
x4 = round(X[3], 1)

# результат
print(f"x1 = {x1}, x2 = {x2}, x3 = {x3}, x4 = {x4}")