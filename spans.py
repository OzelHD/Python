import numpy as np
import matplotlib.pyplot as plt

def plot_infinite_line(p1, p2, ax, label=None, color='b'):

     p1, p2 = np.array(p1), np.array(p2)

     d = p2 - p1
    

     t = np.linspace(-100, 100, 1000)
    
     x = p1[0] + t * d[0]
     y = p1[1] + t * d[1]

     ax.plot(x, y, label=label, color=color)

fig, axs = plt.subplots(1, 2, figsize=(10, 5))

plot_infinite_line((-1, 1), (1, 1), axs[0], label="Span 1", color='r')

plot_infinite_line((1, 0), (1, 1), axs[1], label="Span 2", color='g')

for ax in axs:
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(True)
    ax.legend()

plt.show()