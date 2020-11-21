import numpy as np
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')
 
 
fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
line, = ax.plot([], [], lw=3)
 
def init():
    line.set_data([], [])
    return line,
def animate(i):
    x = np.linspace(0, 4, 1000)
    y = 8*(1 - np.cos(x - 0.1 * i))
    line.set_data(x, y)
    return line,
 
anim = FuncAnimation(fig, animate, init_func=init,
                               frames=1, interval=20, blit=True)
 
 
anim.save('cos_wave.gif', writer='pillow')