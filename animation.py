"""
Dice animation using `matplotlib`
"""

import numpy as np
from simulation import *

DICE_SPOTS = np.array([
    [0.5,0.5,1], # 1
    [0,0.2,0.2],[0,0.8,0.8], # 2
    [0.5,0,0.5],[0.2,0,0.2],[0.8,0,0.8], # 3
    [0.2,1,0.2],[0.8,1,0.8],[0.2,1,0.8],[0.8,1,0.2], # 4
    [1,0.5,0.5],[1,0.8,0.8],[1,0.2,0.2],[1,0.2,0.8],[1,0.8,0.2], # 5
    [0.5,0.8,0],[0.5,0.2,0],[0.8,0.8,0],[0.8,0.2,0],[0.2,0.8,0],[0.2,0.2,0] # 6
])-0.5

def draw_dice_coordinates(x_com, rot):
    points = DICE_SIZE*(np.array([
            [0,0,0],[1,0,0],[1,1,0],[0,1,0],
            [0,0,0],
            [0,0,1],[1,0,1],[1,1,1],[0,1,1],
            [0,1,0],[1,1,0],[1,1,1],[1,0,1],
            [1,0,0],[0,0,0],[0,0,1],[0,1,1]
        ])-0.5)
    coords = []
    for point in points:
        coords.append(x_com + rot @ point.T)
    coords = np.array(coords)
    return coords

def spot_coordinates(x_com, rot):
    points = DICE_SIZE*DICE_SPOTS
    coords = []
    for point in points:
        coords.append(x_com + rot @ point.T)
    coords = np.array(coords)
    return coords

def draw_dice(num_steps, num_dice):
    steps = dice_steps(num_steps, num_dice)
    drawings = []
    scatters = []
    raw_points = []

    for step in steps:
        x0 = step[0][:3]
        rot = step[1]
        drawing = draw_dice_coordinates(x0, rot)
        drawings.append(drawing.T)
        scatter = spot_coordinates(x0, rot)
        scatters.append(scatter.T)
        raw_p = dice_coordinates(x0, rot)
        raw_points.append(raw_p.T)

    drawings = np.array(drawings)
    scatters = np.array(scatters)
    raw_points = np.array(raw_points)
    return [drawings], [scatters], [raw_points]