import itertools
import multiprocessing
import warnings
import numpy as np
from functools import partial
from multiprocessing import Pool
from src.utils import Mentor

def create_angles():
    theta_1 = list(np.linspace(0, 2*3.14159265358979, 100))
    theta_2 = list(np.linspace(0, 2*3.14159265358979, 100))
    theta_3 = list(np.linspace(0, 2*3.14159265358979, 100))
    theta_4 = list(np.linspace(0, 3.14159265358979, 50))
    theta_5 = list(np.linspace(0, 2*3.14159265358979, 100))
    combinations = []
    for element in itertools.product(theta_1, theta_2, theta_3, theta_4, theta_5):
        combinations.append(np.array(element))
    return list(combinations)


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
    return signal, angles
    

if __name__=="__main__":
    robot = Mentor()    
    grid_search(robot)
