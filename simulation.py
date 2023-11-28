"""
Dice simulation

Based on http://www.cs.cmu.edu/~baraff/sigcourse/notesd1.pdf
"""

import numpy as np
import scipy.integrate as integrate

DICE_SIZE = 0.5
DICE_MASS = 0.1
DT = 0.05

I_body = DICE_MASS/12*np.array([
    [2,0,0],
    [0,2,0],
    [0,0,2]
])

def star_mult(vec, mat):
    return np.array([
        [0, -vec[2], vec[1]],
        [vec[2], 0, -vec[0]],
        [-vec[1], vec[0], 0]
    ]) @ mat

def dice_steps(num_steps):
    start_pos = np.array([0,0,0, 0,0,0]) # x, y, z, px, py, pz
    start_rot = np.eye(3)
    start_L = np.array([0,0,0]) # x, y, z
    force = np.array([0,0,-DICE_MASS*9.8])
    torque = np.array([0.2,0,0])
    state = (start_pos, start_rot, start_L)
    
    def dydt(state, force, torque):
        I = state[1] @ I_body @ state[1].T
        omega = (np.linalg.inv(I) @ state[2].T).T
        dxdt = np.array([
            state[0][3]/DICE_MASS, state[0][4]/DICE_MASS, state[0][5]/DICE_MASS,
            force[0], force[1], force[2]
        ])
        dRdt = star_mult(omega, state[1])
        dLdt = torque
        return (dxdt, dRdt, dLdt)

    steps = [state]
    for _ in range(num_steps-1):
        deriv = dydt(state, force, torque)
        new_state = (
            state[0] + deriv[0]*DT,
            state[1] + deriv[1]*DT,
            state[2] + deriv[2]*DT
        )
        steps.append(new_state)
        state = new_state
    
    return steps
