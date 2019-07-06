import itertools
import multiprocessing
import warnings
import random
import math
import numpy as np
from functools import partial
from multiprocessing import Pool
from src.utils import Mentor, Polinomy

def create_angles(theta_i, theta_f, final_time, steps):
    thetas, omegas, times = [], [], []
    for j in range(5):
        theta, omega, time = [], [], []
        theta.append(theta_i[j])
        omega.append(0)
        time.append(0)
        for i in range(steps-2):
            theta.append((theta_f[j] - theta_i[j])*random.random() + theta_i[j])
            omega.append(random.random())
            time.append(final_time*random.random())
        omega.append(0)
        theta.append(theta_f[j])
        time.append(final_time)
        time.sort()
        if theta_i[j] < theta_f[j]:
            theta.sort()
        else:
            theta.sort(reverse=True)    
        omegas.append(omega)
        thetas.append(theta)
        times.append(time)
    return times, thetas, omegas

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

if __name__=="__main__":
    steps = 5
    time = 2
    theta_i = [0, 0, 0, 0, 0]
    theta_f = [3.1415, 3.1415, 3.1415, 3.1415, 3.1415]
    times, thetas, omegas = create_angles(theta_i, theta_f, time, steps)
    mentor = Mentor()
    polynomies = []
    for j in range(steps-1):
        sub_polynomies = []
        for i in range(5):
            sub_polynomies.append(Polinomy(times[i][j], times[i][j+1], thetas[i][j], thetas[i][j+1], omegas[i][j], omegas[i][j+1], number = np.ceil(100*(times[i][j+1] - times[i][j])/time)))
        polynomies.append(sub_polynomies)

    angle_1 = np.array([theta_i[0]])
    angle_2 = np.array([theta_i[1]])
    angle_3 = np.array([theta_i[2]])
    angle_4 = np.array([theta_i[3]])
    angle_5 = np.array([theta_i[4]])
    for i in range(steps-1):
        angle_1 = np.concatenate((angle_1, polynomies[i][0].thetas[1:])) 
        angle_2 = np.concatenate((angle_2, polynomies[i][1].thetas[1:])) 
        angle_3 = np.concatenate((angle_3, polynomies[i][2].thetas[1:])) 
        angle_4 = np.concatenate((angle_4, polynomies[i][3].thetas[1:])) 
        angle_5 = np.concatenate((angle_5, polynomies[i][4].thetas[1:])) 

    index = np.min([angle_1.shape[0], angle_2.shape[0], angle_3.shape[0], angle_4.shape[0], angle_5.shape[0]])
    angle_1 = angle_1[0:index]
    angle_2 = angle_2[0:index]
    angle_3 = angle_3[0:index]
    angle_4 = angle_4[0:index]
    angle_5 = angle_5[0:index]
    angles = []
    angles.append(angle_1)
    angles.append(angle_2)
    angles.append(angle_3)
    angles.append(angle_4)
    angles.append(angle_5)
    angles = np.transpose(angles)
    for angle in angles:
        print(angle)
        print(angle[0])
        print(angle[1])
        print(angle[2])
        print(angle[3])
        print(angle[4])    
        pos, rot = mentor.get_position(angle, 6)
        print('Position: ')
        print(pos[0:3])