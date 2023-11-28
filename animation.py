import numpy as np
from simulation import *

# def draw_dice():
#     start_x0 = 0
#     start_y0 = 0
#     start_z0 = 1
#     start_theta0 = 0
#     start_phi0 = 0
#     t0 = np.arctan(np.sqrt(2))
#     t1 = np.pi-t0
#     start_theta = start_theta0 + np.array([t0,t0,t0,t0,t0,t1,t1,t1,t1,t0,t1,t1,t1,t0,t0,t1])
#     start_phi = start_phi0 + np.array([np.pi/4, 3*np.pi/4, 5*np.pi/4, 7*np.pi/4,np.pi/4,
#                                          np.pi/4, 3*np.pi/4, 5*np.pi/4, 7*np.pi/4,
#                                          7*np.pi/4,7*np.pi/4,np.pi/4,
#                                          3*np.pi/4,3*np.pi/4,5*np.pi/4,5*np.pi/4])
#     start_pos = np.array([
#         start_x0 + DICE_SIZE*np.sin(start_theta)*np.cos(start_phi),
#         start_y0 + DICE_SIZE*np.sin(start_theta)*np.sin(start_phi),
#         start_z0 + DICE_SIZE*np.cos(start_theta)
#     ])
#     steps = [start_pos, start_pos+0.01]
#     steps = np.array(steps)
#     return steps

def draw_dice(num_steps):
    steps = dice_steps(num_steps)
    drawings = []

    for step in steps:
        x0 = step[0][:3]
        rot = step[1]
        points = DICE_SIZE*(np.array([
            [0,0,0],[1,0,0],[1,1,0],[0,1,0],
            [0,0,1],[1,0,1],[1,1,1],[0,1,1]
        ])-0.5)
        drawing = []
        for point in points:
            drawing.append(x0 + rot @ point.T)
        drawing = np.array(drawing)
        drawings.append(drawing.T)

    drawings = np.array(drawings)
    print(drawings.shape)
    return drawings