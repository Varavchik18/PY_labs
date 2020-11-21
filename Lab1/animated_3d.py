from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np
import pandas as pd

X = np.arange(-5, 5, 0.05)
Y = np.arange(-5, 5, 0.05)
X, Y = np.meshgrid(X, Y)
Z = 4 * np.sin(X*Y)


for angle in range(70, 210, 2):
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.set_xlabel('X axes')
    ax.set_ylabel('Y axes')
    ax.set_zlabel('Z axes')

    ax.set_zlim(-4, 8)
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.f'))

    ax.plot_surface(X, Y, Z, color='Turquoise', linewidth=0, antialiased=True, shade = True)
    ax.view_init(30, angle)
 
    filename = 'frames/step'+str(angle)+'.png'
    plt.savefig(filename, dpi=96)
    plt.gca()