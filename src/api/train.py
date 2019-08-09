import itertools
import multiprocessing
import warnings
import random
import math
import numpy as np
from functools import partial
from multiprocessing import Pool
from src.models import Population
from src.utils import Mentor, Polinomy, integration



if __name__=="__main__":
    steps = 3
    time = 10
    robot = Mentor()
    pos = np.zeros(3)
    angles = np.zeros(3)
    pos[0] = input('X i ')
    pos[1] = input('Y i ')
    pos[2] = input('Z i ')
    angles[0] = input('alpha i ')
    angles[1] = input('beta i ')
    angles[2] = input('gamma i ')
    angles[0] = 3.141592*angles[0]/180
    angles[1] = 3.141592*angles[1]/180
    angles[2] = 3.141592*angles[2]/180
    
    rot  = robot.get_orientation(angles[0], angles[1], angles[2])
    matrix_G0 = [[rot[0][0], rot[0][1], rot[0][2], pos[0]],
    [rot[1][0], rot[1][1], rot[1][2], pos[1]],
    [rot[2][0], rot[2][1], rot[2][2], pos[2]],
    [0, 0, 0, 1]]
    rotation = [[rot[0][0], rot[0][1], rot[0][2]],
    [rot[1][0], rot[1][1], rot[1][2]],
    [rot[2][0], rot[2][1], rot[2][2]]]
    matrix_5G = [[1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, -6],
    [0, 0, 0, 1]]
    matrix = np.matmul(matrix_G0, matrix_5G)
    positions = [matrix[0][3], matrix[1][3], matrix[2][3]]
    theta_i = robot.get_angles(positions,rotation)
    print(theta_i)
    pos, rot = robot.get_position(theta_i, 6)
    print(pos)
    print(rot)
    pos[0] = input('X f ')
    pos[1] = input('Y f ')
    pos[2] = input('Z f ')
    angles[0] = input('alpha f ')
    angles[1] = input('beta f ')
    angles[2] = input('gamma f ')
    angles[0] = 3.141592*angles[0]/180
    angles[1] = 3.141592*angles[1]/180
    angles[2] = 3.141592*angles[2]/180
    rot  = robot.get_orientation(angles[0], angles[1], angles[2])
    matrix_G0 = [[rot[0][0], rot[0][1], rot[0][2], pos[0]],
    [rot[1][0], rot[1][1], rot[1][2], pos[1]],
    [rot[2][0], rot[2][1], rot[2][2], pos[2]],
    [0, 0, 0, 1]]
    matrix_5G = [[1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, -6],
    [0, 0, 0, 1]]
    matrix = np.matmul(matrix_G0, matrix_5G)
    positions = [matrix[0][3], matrix[1][3], matrix[2][3]]
    theta_f = robot.get_angles(positions, rot)
    print(theta_f)
    pos, rot = robot.get_position(theta_f, 6)
    print(pos)
    #theta_i = [0, 0, 0, 0, 0]
#   theta_f = [3.1415, 3.1415/6, 3.1415/6, 3.1415/2, 3.1415/2]
    optimized = Population(100, 30, 30, 0.7, 0.04, theta_i, theta_f, time, steps)
    population = optimized.initialization(theta_i, theta_f, time, steps)

    optimized.generation(population, theta_i, theta_f, time, steps)
        