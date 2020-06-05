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
    theta = robot.get_angles(positions, rot)
    return theta

if __name__ == "__main__":
    steps = 3
    time = 10
    robot = Mentor()
    pos, angles = input_cartesian()    
    theta_i = calculate_thetas(pos, angles)
    pos, angles = input_cartesian()
    theta_f = calculate_thetas(pos, angles)    
    optimized = Population(10, 1, 5, 0.7, 0.04, theta_i, theta_f, time, steps, pos)
    population = optimized.initialization(theta_i, theta_f, time, steps)
    optimized.generation(population, theta_i, theta_f, time, steps)
       