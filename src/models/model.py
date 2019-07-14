import itertools
import multiprocessing
import warnings
import random
import numpy as np
from functools import partial
from multiprocessing import Pool
from src.utils import Mentor, Polinomy
from src.utils.numerical import integration, create_angles


class Node:
    def __init__(self, theta_i, theta_f, time, steps):
        polynomies = []
        self.times, self.thetas, self.omegas = create_angles(theta_i, theta_f, time, steps)
        self.mentor = Mentor()
        for j in range(steps-1):
            sub_polynomies = []
            for i in range(5):
                sub_polynomies.append(Polinomy(times[i][j], times[i][j+1], thetas[i][j], thetas[i][j+1], omegas[i][j], omegas[i][j+1], number = np.ceil(1000*(times[i][j+1] - times[i][j])/time)))
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
        points = []
        for angle in angles:
            pos, rot = mentor.get_position(angle, 6)
            points.append(pos[0:3])
        
        integration(np.array(points))