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
    for i in range(100):
        times, thetas, omegas = create_angles(theta_i, theta_f, time, steps)
        mentor = Mentor()
        polynomies = []

        for j in range(steps-1):
            sub_polynomies = []
            for i in range(4):
                sub_polynomies.append(Polinomy(times[i][j], times[i][j+1], thetas[i][j], thetas[i][j+1], omegas[i][j], omegas[i][j+1], number = np.ceil(100000*(times[i][j+1] - times[i][j])/time)))
            polynomies.append(sub_polynomies)

        angle_1 = np.array([theta_i[0]])
        angle_2 = np.array([theta_i[1]])
        angle_3 = np.array([theta_i[2]])
        angle_4 = np.array([theta_i[3]])
        omega_1 = np.array([0])
        omega_2 = np.array([0])
        omega_3 = np.array([0])
        omega_4 = np.array([0])
        for i in range(steps-1):
            angle_1 = np.concatenate((angle_1, polynomies[i][0].thetas[1:])) 
            angle_2 = np.concatenate((angle_2, polynomies[i][1].thetas[1:])) 
            angle_3 = np.concatenate((angle_3, polynomies[i][2].thetas[1:])) 
            angle_4 = np.concatenate((angle_4, polynomies[i][3].thetas[1:])) 
            omega_1 = np.concatenate((omega_1, polynomies[i][0].delta_thetas[1:])) 
            omega_2 = np.concatenate((omega_2, polynomies[i][1].delta_thetas[1:])) 
            omega_3 = np.concatenate((omega_3, polynomies[i][2].delta_thetas[1:])) 
            omega_4 = np.concatenate((omega_4, polynomies[i][3].delta_thetas[1:])) 

        index = min([angle_1.shape[0], angle_2.shape[0], angle_3.shape[0], angle_4.shape[0]])
        dist_4, dist_3, dist_2, dist_1 = 0, 0, 0, 0

        for i in range(index):
            dist_4+=6*omega_4[i]*(time/angle_4.shape[0])
            
            dist_3+=omega_3[i]*np.sqrt(36 - 12*mentor.a[3]*np.sin(angle_4[i])+ np.power(mentor.a[3], 2))*(time/angle_3.shape[0])
            
            dist_2+=omega_2[i]*np.sqrt(36+np.power(mentor.a[2], 2)+np.power(mentor.a[3], 2)+2*mentor.a[2]*mentor.a[3]*np.cos(angle_3[i])-12*mentor.a[2]*np.sin(angle_4[i] + angle_3[i])
            -12*mentor.a[3]*np.sin(angle_4[i]))*(time/angle_2.shape[0])
        
            dist_1+=omega_1[i]*np.sqrt(np.power(mentor.a[2]*np.cos(angle_2[i]) + 
            mentor.a[3]*np.cos(angle_2[i] + angle_3[i]) - 
            6*np.sin(angle_2[i] + angle_3[i] + angle_4[i]), 2))*(time/angle_1.shape[0])
        
        print(dist_1 + dist_2 + dist_3 + dist_4)
