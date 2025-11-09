import matplotlib.pyplot as plt
import numpy as np

#  в градусах
x = np.linspace(-360, 360, 800)

#  в радианы
x_rad = np.radians(x)

# Первая функция
y1 = np.exp(np.cos(x_rad)) + np.log(np.cos(0.6 * x_rad)**2 + 1) * np.sin(x_rad)

# Вторая функция
y2 = -np.log((np.cos(x_rad) + np.sin(x_rad))**2 + 2.5) + 10

# графики
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(x, y1, color='blue')
plt.title('f(x)')
plt.xlabel('x (градусы)')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(x, y2, color='red')
plt.title('h(x)')
plt.xlabel('x (градусы)')
plt.grid(True)

plt.tight_layout()
plt.show()