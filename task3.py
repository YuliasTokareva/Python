import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.axis('off')

# Цвета
face_color = '#f4c542'     # золотистый
mane_color = '#e67e22'     # оранжевый
nose_color = '#5d3a00'     # тёмно-коричневый

# Хвост
tail_arc = patches.Arc((6.5, 3.5), 4, 4, theta1=230, theta2=15, color=mane_color, linewidth=6)
tail_tip = patches.Circle((8.5, 4), 0.3, facecolor=mane_color)
ax.add_patch(tail_arc)
ax.add_patch(tail_tip)

# Тело
body = patches.Ellipse((5, 3), 4.5,5.5, facecolor=face_color)
ax.add_patch(body)

# Лапы
ax.add_patch(patches.Ellipse((4, 0.4), 1.2, 0.8, facecolor=face_color))
ax.add_patch(patches.Ellipse((6.2, 0.4), 1.2, 0.8, facecolor=face_color))
ax.add_patch(patches.Ellipse((2.80, 2.20), 1.2, 0.8, facecolor=face_color))
ax.add_patch(patches.Ellipse((7.2, 2.20), 1.2, 0.8, facecolor=face_color))


# Грива — 14 кружков
for angle in np.linspace(0, 2*np.pi, 14, endpoint=False):
    x = 5 + 2.4 * np.cos(angle)
    y = 5 + 2.4 * np.sin(angle)
    mane = patches.Circle((x, y), 0.7, facecolor=mane_color)
    ax.add_patch(mane)

# Уши
ax.add_patch(patches.Circle((3.67, 6.32), 0.7, facecolor=face_color))
ax.add_patch(patches.Circle((6.32, 6.32), 0.7, facecolor=face_color))
ax.add_patch(patches.Circle((3.57, 6.44), 0.3, facecolor=mane_color))
ax.add_patch(patches.Circle((6.44, 6.44), 0.3, facecolor=mane_color))

# Голова
head = patches.Circle((5, 5), 2, facecolor=face_color)
ax.add_patch(head)


# Глаза
ax.add_patch(patches.Circle((4.3, 5.5), 0.3, facecolor='white'))
ax.add_patch(patches.Circle((5.7, 5.5), 0.3, facecolor='white'))
ax.add_patch(patches.Circle((4.3, 5.5), 0.15, facecolor='black'))
ax.add_patch(patches.Circle((5.7, 5.5), 0.15, facecolor='black'))

# Нос
nose = patches.RegularPolygon((5.0, 4.6), numVertices=3, radius=0.2, orientation=np.pi, facecolor=nose_color)
ax.add_patch(nose)

# Рот
ax.plot([5.0, 5.0], [4.4, 4.2], color=nose_color, linewidth=2)
ax.plot([5.0, 4.8], [4.2, 4.0], color=nose_color, linewidth=2)
ax.plot([5.0, 5.2], [4.2, 4.0], color=nose_color, linewidth=2)

# Усы — треугольником
for dx, dy in [(-0.6, 0.15), (-0.6, -0.15)]:
    ax.add_patch(patches.Circle((5.0 + dx, 4.3 + dy), 0.05, facecolor=nose_color))
for dx, dy in [(0.6, 0.15), (0.6, -0.15)]:
    ax.add_patch(patches.Circle((5.0 + dx, 4.3 + dy), 0.05, facecolor=nose_color))
for dx in [-0.3, -0.5, -0.7]:
    ax.add_patch(patches.Circle((5.0 + dx, 4.3), 0.05, facecolor=nose_color))
for dx in [0.3, 0.5, 0.7]:
    ax.add_patch(patches.Circle((5.0 + dx, 4.3), 0.05, facecolor=nose_color))
plt.show()
