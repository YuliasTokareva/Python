import matplotlib.pyplot as plt
import numpy as np

# создаём три диапазона x чтобы не было лишних линий
x1 = np.linspace(-10, -3.1, 300)   # слева от x = -3
x2 = np.linspace(-2.9, 2.9, 300)   # между асимптотами
x3 = np.linspace(3.1, 10, 300)     # справа от x = 3

# считаем f(x) для каждого диапазона
f1 = 5 / (x1**2 - 9)
f2 = 5 / (x2**2 - 9)
f3 = 5 / (x3**2 - 9)

# Рисуем три куска графика
plt.plot(x1, f1, color='blue')
plt.plot(x2, f2, color='blue')
plt.plot(x3, f3, color='blue')

#  сетка и подписи
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График f(x) = 5/(x² - 9)')

# итог
plt.show()