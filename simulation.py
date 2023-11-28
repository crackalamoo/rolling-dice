"""
Dice simulation

Based on http://www.cs.cmu.edu/~baraff/sigcourse/notesd1.pdf
"""

DICE_SIZE = 0.5

import numpy as np
import scipy.integrate as integrate

def dice_steps(num_steps):
    start_pos = np.array([0,0,1, 0,0]) # x, y, z, 