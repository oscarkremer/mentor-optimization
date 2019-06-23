import itertools
import multiprocessing
import warnings
import random
import numpy as np
from functools import partial
from multiprocessing import Pool
from src.utils import Mentor

def create_angles(theta_i, theta_f):
    thetas = []
    for j in range(5):
        theta = []
        for i in range(5):
            theta.append((theta_f[j] - theta_i[j])*random.random() + theta_i[j])
        if theta_i[j] < theta_f[j]:
            theta.sort()
        else:
            theta.sort(reverse=True)    
        thetas.append(theta)
    print(thetas)

def grid_search(robot):
    execute_grid_search(robot)


def execute_grid_search(robot):
    angles = create_angles()
    pool = Pool(multiprocessing.cpu_count())
    results = pool.map(partial(find_colision), angles)
    pool.close()
    pool.join()
    print(results)


def find_colision(angles):
    pos_ext, _ = robot.get_position(angles, 6)
    pos_axis, _ = robot.get_position(angles, 0)
    signal = True
    print("Random float number is ", random.random())

    return signal, angles
    

if __name__=="__main__":
    theta_i = [0, 0, 0, 0, 0]
    theta_f = [3.1415, 3.1415, 3.1415, 3.1415, 3.1415]
    create_angles(theta_i, theta_f)