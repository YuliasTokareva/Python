import numpy as np
from scipy import integrate

# одинарный интеграл
def f1(x):
    return x * np.exp(-x**2) * np.log(x)

result1 = integrate.quad(f1, 1, 3)[0]# 0 для того чтобы вывоилось только число без погрешности

# двойной интеграл
def integrand(x, y):
    return np.sqrt(1 + x**2 * y)

result2 = integrate.dblquad(integrand, 0, 1, 0, 2)[0]

# Выводим результаты
print(f"Одинарный интеграл: {result1:.6f}")
print(f"Двойной интеграл: {result2:.6f}")