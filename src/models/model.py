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
        times, thetas, omegas = [], [], []
        for i in range(5):
            deltas, delta_thetas, delta_omegas = create_angles(theta_i[i], theta_f[i], time, steps)
            times.append(deltas)
            thetas.append(delta_thetas)
            omegas.append(delta_omegas)
        self.joint1 = [times[0], thetas[0], omegas[0]]
        self.joint2 = [times[1], thetas[1], omegas[1]]
        self.joint3 = [times[2], thetas[2], omegas[2]]
        self.joint4 = [times[3], thetas[3], omegas[3]]
        self.joint5 = [times[4], thetas[4], omegas[4]]
        self.dist_calc(steps, theta_i, time)


    def dist_calc(self, steps, theta_i, time):
        mentor = Mentor()
        angles, points, polynomies = [], [], []
        for j in range(steps-1):
            sub_polynomies = []
            sub_polynomies.append(Polinomy(self.joint1[0][j], self.joint1[0][j+1], self.joint1[1][j], self.joint1[1][j+1], self.joint1[2][j], self.joint1[2][j+1], number = np.ceil(1000*(self.joint1[0][j+1] - self.joint1[0][j])/time)))
            sub_polynomies.append(Polinomy(self.joint2[0][j], self.joint2[0][j+1], self.joint2[1][j], self.joint2[1][j+1], self.joint2[2][j], self.joint2[2][j+1], number = np.ceil(1000*(self.joint2[0][j+1] - self.joint2[0][j])/time)))
            sub_polynomies.append(Polinomy(self.joint3[0][j], self.joint3[0][j+1], self.joint3[1][j], self.joint3[1][j+1], self.joint3[2][j], self.joint3[2][j+1], number = np.ceil(1000*(self.joint3[0][j+1] - self.joint3[0][j])/time)))
            sub_polynomies.append(Polinomy(self.joint4[0][j], self.joint4[0][j+1], self.joint4[1][j], self.joint4[1][j+1], self.joint4[2][j], self.joint4[2][j+1], number = np.ceil(1000*(self.joint4[0][j+1] - self.joint4[0][j])/time)))
            sub_polynomies.append(Polinomy(self.joint5[0][j], self.joint5[0][j+1], self.joint5[1][j], self.joint5[1][j+1], self.joint5[2][j], self.joint5[2][j+1], number = np.ceil(1000*(self.joint5[0][j+1] - self.joint5[0][j])/time)))
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
        angles = np.transpose([angle_1[0:index], angle_2[0:index], angle_3[0:index], angle_4[0:index], angle_5[0:index]])
        for angle in angles:
            pos, rot = mentor.get_position(angle, 6)
            points.append(pos[0:3])
        self.points = points
        self.dist = integration(np.array(points))