import numpy as np
from src.models import Population
from src.utils import Mentor
from src.utils.input import input_cartesian

def calculate_thetas(pos, angles):
    robot = Mentor()
    rot  = robot.get_orientation(angles[0], angles[1], angles[2])
    matrix_G0 = [[rot[0][0], rot[0][1], rot[0][2], pos[0]],
    [rot[1][0], rot[1][1], rot[1][2], pos[1]],
    [rot[2][0], rot[2][1], rot[2][2], pos[2]],
    [0, 0, 0, 1]]
    matrix_5G = [[1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, -5],
    [0, 0, 0, 1]]
    matrix = np.matmul(matrix_G0, matrix_5G)
    positions = [matrix[0][3], matrix[1][3], matrix[2][3]]
    error, theta = robot.get_angles(positions, rot)
    return error, theta

def enter_position():
    error = True
    while error:
        pos, angles = input_cartesian()    
        error, theta = calculate_thetas(pos, angles)
        if error:
            print('Error - Impossible position and/or orientation, please enter other values')
    return theta, pos

if __name__ == "__main__":
    steps = 3
    time = 10
    theta_i, pos_i = enter_position()
    theta_f, pos_f = enter_position()
    optimized = Population(30, 10, 30, 0.7, 0.3, theta_i, theta_f, time, steps, pos_f)
    population = optimized.initialization(theta_i, theta_f, time, steps)
    optimized.generation(population, theta_i, theta_f, time, steps)
       