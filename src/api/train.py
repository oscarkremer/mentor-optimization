import itertools
import multiprocessing
import warnings
import random
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
        times.sort()
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
    steps = 3
    time = 4
    theta_i = [0, 0, 0, 0, 0]
    theta_f = [3.1415, 3.1415, 3.1415, 3.1415, 3.1415]
    times, thetas, omegas = create_angles(theta_i, theta_f, time, steps)
    print(times)
    print(thetas)
    print(omegas)
    mentor = Mentor()
    dist_4, dist_3, dist_2, dist_1 = 0, 0, 0, 0
    poly_1 = Polinomy(times[0][0], times[0][1], thetas[0][0], thetas[0][1], omegas[0][0], omegas[0][1])
    poly_2 = Polinomy(times[1][0], times[1][1], thetas[1][0], thetas[1][1], omegas[1][0], omegas[1][1])
    poly_3 = Polinomy(times[2][0], times[2][1], thetas[2][0], thetas[2][1], omegas[2][0], omegas[2][1])
    poly_4 = Polinomy(times[3][0], times[3][1], thetas[3][0], thetas[3][1], omegas[3][0], omegas[3][1])
    dist_4, dist_3, dist_2, dist_1 = 0, 0, 0, 0
    time_malha = np.linspace(0, time, 10000)
    for i in range(10000):
        for 
        if time_malha[i]<times[0][1]:
            angulo[0][i] = poly_1.thetas[i]
            delta_angulo[0][i] = poly_1.delta_thetas[i]


    for i in range(poly_1.steps):
        dist_4+=6*poly_4.delta_thetas[i]*(time/poly_1.steps)
        dist_3+=poly_3.delta_thetas[i]*np.sqrt(36 - 12*mentor.a[3]*np.sin(poly_4.thetas[i])+ np.power(mentor.a[3], 2))*(time/poly_1.steps)
        dist_2+=poly_2.delta_thetas[i]*np.sqrt(36+np.power(mentor.a[2], 2)+np.power(mentor.a[3], 2)+2*mentor.a[2]*mentor.a[3]*np.cos(poly_3.thetas[i])-12*mentor.a[2]*np.sin(poly_4.thetas[i] + poly_3.thetas[i])
        -12*mentor.a[3]*np.sin(poly_4.thetas[i]))*(time/poly_1.steps)
        dist_1+=poly_1.delta_thetas[i]*np.sqrt(np.power(mentor.a[2]*np.cos(poly_2.thetas[i]) + 
        mentor.a[3]*np.cos(poly_2.thetas[i] + poly_3.thetas[i]) - 
        6*np.sin(poly_2.thetas[i]+poly_3.thetas[i]+poly_4.thetas[i]), 2))*(time/poly_1.steps)
    print(dist_1 + dist_2 + dist_3 + dist_4)
