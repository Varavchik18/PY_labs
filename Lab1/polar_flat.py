import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


plt.style.use('seaborn-pastel')


fig = plt.figure()
ax = plt.axes(xlim=(-2*np.pi, 2*np.pi), ylim=(0, 11))
line = ax.plot([], [], lw=3, label = "r=8(1-cos(x))")
 
def init():
    line.set_data([], [])
    return line
def animate(i):
    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    y = np.sin(x)
    line.set_data(x, y)
    return line
 
anim = FuncAnimation(fig, animate, init_func=init,
                               frames=250, interval=30, blit=True)
 
 
anim.save('cos_wave.gif', writer='pillow')