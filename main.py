import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from simulation import *

N_STEPS = 2

def update_lines(num, step_arrs, lines):
    for line, steps in zip(lines, step_arrs):
        line.set_data(steps[num, :2])
        line.set_3d_properties(steps[num, 2])
    return lines

dice = [dice_steps(N_STEPS)]

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

lines = [ax.plot([], [], [])[0] for _ in dice]

ax.set(xlim3d=(-1, 1), xlabel='X')
ax.set(ylim3d=(-1, 1), ylabel='Y')
ax.set(zlim3d=(0, 1), zlabel='Z')
ax.set_aspect('equal')

ani = animation.FuncAnimation(
    fig, update_lines, N_STEPS, fargs=(dice, lines), interval=100)

plt.show()
