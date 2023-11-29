"""
Dice animation using `matplotlib`
"""

import numpy as np
from simulation import *

def draw_dice(num_steps, num_dice):
    steps = dice_steps(num_steps, num_dice)
    drawings = []

    for step in steps:
        x0 = step[0][:3]
        rot = step[1]
        drawing = dice_coordinates(x0, rot)
        drawings.append(drawing.T)

    drawings = np.array(drawings)
    print(drawings.shape)
    return [drawings]