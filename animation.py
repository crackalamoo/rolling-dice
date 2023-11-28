"""
Dice animation using `matplotlib`
"""

import numpy as np
from simulation import *

def draw_dice(num_steps):
    steps = dice_steps(num_steps)
    drawings = []

    for step in steps:
        x0 = step[0][:3]
        rot = step[1]
        points = DICE_SIZE*(np.array([
            [0,0,0],[1,0,0],[1,1,0],[0,1,0],
            [0,0,0],
            [0,0,1],[1,0,1],[1,1,1],[0,1,1],
            [0,1,0],[1,1,0],[1,1,1],[1,0,1],
            [1,0,0],[0,0,0],[0,0,1],[0,1,1]
        ])-0.5)
        drawing = []
        for point in points:
            drawing.append(x0 + rot @ point.T)
        drawing = np.array(drawing)
        drawings.append(drawing.T)

    drawings = np.array(drawings)
    print(drawings.shape)
    return drawings