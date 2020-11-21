from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np
import pandas as pd


# Створюємо дані для вісей
X = np.arange(-12, 12, 0.05)
Y = np.arange(-12, 12, 0.05)

# Створюємо сітку для правильного відображення графіка і 
# корректної роботи функції plot_surface
X, Y = np.meshgrid(X, Y)
Z = X**2
Z2 = 1 - Y**2

# Робимо 70 графіків від 70 градусів до 210 з кроком в 2 градуси
for angle in range(70, 210, 2):
    # Створюємо тривимірні вісі
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Даємо імена осям
    ax.set_xlabel('X axes')
    ax.set_ylabel('Y axes')
    ax.set_zlabel('Z axes')

    # Змінюємо вісь Z, ставимо діпазон від [-4; 8].
    ax.set_zlim(-100, 100)
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.f'))

    ax.plot_surface(X, Y, Z, color='Green', linewidth=0, antialiased=True, shade = True)
    ax.plot_surface(X, Y, Z2, color='Blue', linewidth=0, antialiased=True, shade = True)
    ax.view_init(30, angle)
 
    filename = 'frames/step'+str(angle)+'.png'
    plt.savefig(filename, dpi=96)
    plt.gca()