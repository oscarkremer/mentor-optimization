import random
import numpy as np
from functools import partial
from src.utils import Mentor, Polinomy
from src.utils.numerical import create_angles

class Node:
    def __init__(self, theta_i, theta_f, time, steps, final_point):
        self.x = final_point[0]
        self.y = final_point[1]
        self.z = final_point[2]
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

    def find_points(self, theta_i, time, steps):    
        mentor = Mentor()
        angles, points, polynomies = [], [], []
        for j in range(steps-1):
            sub_polynomies = []
            sub_polynomies.append(Polinomy(self.joint1[0][j], self.joint1[0][j+1], self.joint1[1][j], self.joint1[1][j+1], self.joint1[2][j], self.joint1[2][j+1], number = np.ceil(150*(self.joint1[0][j+1] - self.joint1[0][j])/time)))
            sub_polynomies.append(Polinomy(self.joint2[0][j], self.joint2[0][j+1], self.joint2[1][j], self.joint2[1][j+1], self.joint2[2][j], self.joint2[2][j+1], number = np.ceil(150*(self.joint2[0][j+1] - self.joint2[0][j])/time)))
            sub_polynomies.append(Polinomy(self.joint3[0][j], self.joint3[0][j+1], self.joint3[1][j], self.joint3[1][j+1], self.joint3[2][j], self.joint3[2][j+1], number = np.ceil(150*(self.joint3[0][j+1] - self.joint3[0][j])/time)))
            sub_polynomies.append(Polinomy(self.joint4[0][j], self.joint4[0][j+1], self.joint4[1][j], self.joint4[1][j+1], self.joint4[2][j], self.joint4[2][j+1], number = np.ceil(150*(self.joint4[0][j+1] - self.joint4[0][j])/time)))
            sub_polynomies.append(Polinomy(self.joint5[0][j], self.joint5[0][j+1], self.joint5[1][j], self.joint5[1][j+1], self.joint5[2][j], self.joint5[2][j+1], number = np.ceil(150*(self.joint5[0][j+1] - self.joint5[0][j])/time)))
            polynomies.append(sub_polynomies)
        angles = [np.array([theta_i[i]]) for i in range(5)]
        for i in range(steps-1):
            for j in range(len(angles)):
                angles[j] = np.concatenate((angles[j], polynomies[i][j].thetas[1:])) 
        index = np.min([angles[0].shape[0], angles[1].shape[0], angles[2].shape[0], angles[3].shape[0], angles[4].shape[0]])
        self.angle_1 = angles[0][0:index]
        self.angle_2 = angles[1][0:index]
        self.angle_3 = angles[2][0:index]
        self.angle_4 = angles[3][0:index]
        self.angle_5 = angles[4][0:index]
        angles = np.transpose([self.angle_1, self.angle_2, self.angle_3, self.angle_4, self.angle_5])
        dist = 0 
        for i, angle in enumerate(angles):
            new_pos, rot = mentor.get_position(angle, z_axis=5)
            if i == 0:
                old_pos = new_pos
            else:
                dist+=np.sqrt((old_pos[0]-new_pos[0])**2+(old_pos[1]-new_pos[1])**2+(old_pos[2]-new_pos[2])**2)
                old_pos = new_pos
            points.append(new_pos[0:3])
        self.dist = dist
        self.points = points
        self.constraint = False
        self.test_velocity(time)

    def test_velocity(self, time):
        for i in range(self.angle_1.shape[0]-1):
            if abs(self.angle_1[i+1]-self.angle_1[i])/(time/self.angle_1.shape[0]) > 6 or self.final_points():
                self.constraint = True
            if abs(self.angle_2[i+1] - self.angle_2[i])/(time/self.angle_1.shape[0]) > 6 or self.final_points():
                self.constraint = True
            if abs(self.angle_3[i+1] - self.angle_3[i])/(time/self.angle_1.shape[0]) > 6 or self.final_points():
                self.constraint = True
            if abs(self.angle_4[i+1] - self.angle_4[i])/(time/self.angle_1.shape[0]) > 6 or self.final_points():
                self.constraint = True
            if abs(self.angle_5[i+1] - self.angle_5[i])/(time/self.angle_1.shape[0]) > 6 or self.final_points():
                self.constraint = True

    def final_points(self):
        tol=0.01
        if abs(self.points[-1][0]-self.x)>tol or abs(self.points[-1][1]-self.y)>tol or abs(self.points[-1][2]-self.z)>tol:
            print('here')
            return True
        else:
            return False
