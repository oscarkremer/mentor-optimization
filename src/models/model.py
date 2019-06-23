import itertools
import multiprocessing
import warnings
import random
import numpy as np
from functools import partial
from multiprocessing import Pool
from src.utils import Mentor


class Node:
def create_angles(theta_i, theta_f, time, steps):
    thetas, deltas = [], []
    for j in range(5):
        theta = []
        for i in range(steps-1):
            theta.append((theta_f[j] - theta_i[j])*random.random() + theta_i[j])
        theta.append(theta_f[j])
        if theta_i[j] < theta_f[j]:
            theta.sort()
        else:
            theta.sort(reverse=True)    
        deltas.append(derivative(theta, time/steps))
        thetas.append(theta)
    return thetas, deltas

def derivative(theta, delta):
    derivative = []
    for i in range(len(theta)):
        if i == 0:
            derivative.append(0)
        else:
            derivative.append((theta[i] - theta[i-1])/delta)
    return derivative

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
    for i in range(1000):
        time = 4
        theta_i = [0, 0, 0, 0, 0]
        theta_f = [3.1415, 3.1415, 3.1415, 3.1415, 3.1415]
        thetas, delta_thetas = create_angles(theta_i, theta_f, time, 1000)
        mentor = Mentor()
        dist_4, dist_3, dist_2, dist_1 = 0, 0, 0, 0

        for i in range(1000):
            dist_4+=6*delta_thetas[3][i]*(time/1000)

        for i in range(1000):
            dist_3+=delta_thetas[2][i]*np.sqrt(36 - 12*mentor.a[3]*np.sin(thetas[3][i])+ np.power(mentor.a[3], 2))*(time/1000)

        for i in range(1000):
            dist_2+=delta_thetas[1][i]*np.sqrt(36+np.power(mentor.a[2], 2)+np.power(mentor.a[3], 2)+2*mentor.a[2]*mentor.a[3]*np.cos(thetas[2][i])-12*mentor.a[2]*np.sin(thetas[3][i] + thetas[2][i])
            -12*mentor.a[3]*np.sin(thetas[3][i]))*(time/1000)

        for i in range(1000):
            dist_1+=delta_thetas[0][i]*np.sqrt(np.power(mentor.a[2]*np.cos(thetas[1][i]) + 
            mentor.a[3]*np.cos(thetas[1][i] + thetas[2][i]) - 
            6*np.sin(thetas[1][i] + thetas[2][i] + thetas[3][i]), 2))*(time/1000)

        print(abs(dist_4) + abs(dist_3) + abs(dist_2) + abs(dist_1))

