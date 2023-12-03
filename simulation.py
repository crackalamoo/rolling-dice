"""
Dice simulation

Based on [An Introduction to Physically Based Modeling](http://www.cs.cmu.edu/~baraff/sigcourse/notesd1.pdf)
([part 2](http://www.cs.cmu.edu/~baraff/sigcourse/notesd2.pdf))
by David Baraff, Carnegie Mellon University
"""

import numpy as np
import scipy.integrate as integrate

DICE_SIZE = 0.5
DICE_MASS = 0.1
DT = 0.01
BOUNCE = 0.0
COLLISION_EPS = 1e-2

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

def dice_coordinates(x_com, rot):
    points = DICE_SIZE*(np.array([
            [0,0,0],[1,0,0],[1,1,0],[0,1,0],
            [0,0,1],[1,0,1],[1,1,1],[0,1,1]
        ])-0.5)
    coords = []
    for point in points:
        coords.append(x_com + rot @ point.T)
    coords = np.array(coords)
    return coords



def dice_steps(num_steps, num_dice):
    start_pos = np.array([2*np.random.random()-1,2*np.random.random()-1,0.8,
                          0,0,0]) # x, y, z, px, py, pz
    start_rot = np.eye(3)
    start_L = np.array([0.05,0.01,0]) # x, y, z
    force = np.array([0,0,-DICE_MASS*9.8])
    torque = np.array([0,0,0])
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
        new_state = [
            state[0] + deriv[0]*DT,
            state[1] + deriv[1]*DT,
            state[2] + deriv[2]*DT
        ]
        x0 = state[0][:3]
        rot = state[1]
        coords = dice_coordinates(x0, rot)

        contact_points = 0
        under_floor = 0
        linear_impulse = 0
        I = state[1] @ I_body @ state[1].T
        omega = (np.linalg.inv(I) @ state[2].T).T
        lowest_point = -1
        for i in range(len(coords)):
            point = coords[i]
            if point[2] < COLLISION_EPS:
                contact_points += 1
                if -point[2] > under_floor:
                    under_floor = -point[2]
                    lowest_point = i
                point_momentum = state[0][3:] + DICE_MASS*np.cross(omega, point - x0)
                point_impulse = -point_momentum[2] * (1.0+BOUNCE)
                linear_impulse = max(linear_impulse, point_impulse)
        if contact_points > 0:
            new_state[0][2] += under_floor
            if under_floor > COLLISION_EPS:
                contact = coords[lowest_point] - x0
                angular_impulse = np.cross(contact, np.array([0,0,linear_impulse]))
                new_state[0][5] += linear_impulse
                new_state[2] += angular_impulse

        steps.append(new_state)
        state = new_state
    
    return steps
