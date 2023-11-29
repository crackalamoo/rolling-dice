import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from simulation import *
from animation import *

N_STEPS = 700
TIME_SCALE = 1.0 # 1.0 is real-time animation speed

def update_lines(num, step_arrs, lines, plots):
    for line, steps in zip(lines, step_arrs[0]):
        line.set_data(steps[num, :2])
        line.set_3d_properties(steps[num, 2])
        # plt.gca().add_collection3d(Poly3DCollection([list(zip(steps[num, 0], steps[num, 1], steps[num, 2]))]))
    for plot, steps in zip(plots, step_arrs[1]):
        plot._offsets3d = (steps[num, 0], steps[num, 1], steps[num, 2])
    return lines

dice = draw_dice(N_STEPS, 1)

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

lines = [ax.plot([], [], [])[0] for _ in dice[0]]
plots = [ax.scatter([], [], [], c='g') for _ in dice[1]]
print(dice[2][0].shape)
# collections = [Poly3DCollection([list(zip(steps[0, 0], steps[0, 1], steps[0, 2]))]) for steps in dice[2]]
# ax.add_collection3d(collections[0])

ax.set(xlim3d=(-1, 1), xlabel='X')
ax.set(ylim3d=(-1, 1), ylabel='Y')
ax.set(zlim3d=(0, 1), zlabel='Z')
ax.set_aspect('equal')

ani = animation.FuncAnimation(
    fig, update_lines, N_STEPS, fargs=(dice, lines, plots), interval=DT*1000*TIME_SCALE)

plt.show()
