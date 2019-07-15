import numpy as np

class Mentor:
    def __init__(self):
        self.alpha = [0, -np.pi/2, 0, 0, -np.pi/2]
        self.a = [0, 0, 17.2739, 15.5, 0]
        self.d = [0, 0, 0, 0, 0]
        
    def get_angles(self, pos, rot):
        orientation = rot 
        theta = []
        theta1 = np.arctan(pos[1]/pos[0])
        theta3 = np.arccos((pos[0]**2 + pos[1]**2 + pos[2]**2 - self.a[2]**2 - self.a[3]**2)/(2*self.a[2]*self.a[3]))
        theta3 = np.nan_to_num(theta3)
        theta2 = -theta3 + np.arcsin(((-np.cos(theta3)*self.a[2] - self.a[3])*pos[2] + np.sin(theta3)*self.a[2]*(np.sin(theta1)*pos[1]+pos[0]*np.cos(theta1)))/(np.power(np.cos(theta1)*pos[0]+np.sin(theta1)*pos[1], 2)+ pos[2]*pos[2]))
        sin_theta4 = np.sin(theta2+theta3)*orientation[2][2] - np.cos(theta1)*np.cos(theta2+theta3)*orientation[0][2] - np.sin(theta1)*np.cos(theta2+theta3)*orientation[1][2]
        cos_theta4 = -np.cos(theta2+theta3)*orientation[2][2] - np.cos(theta1)*np.sin(theta2+theta3)*orientation[0][2] - np.sin(theta1)*np.sin(theta2+theta3)*orientation[1][2]
        theta4 = self.fix_quadrante(sin_theta4, cos_theta4)
        sin_theta5 = np.sin(theta1)*orientation[0][0] - np.cos(theta1)*orientation[1][0]
        cos_theta5 = np.sin(theta1)*orientation[0][1] - np.cos(theta1)*orientation[1][1]
        theta5  = self.fix_quadrante(sin_theta5, cos_theta5)
        theta.append(theta1)
        theta.append(theta2)
        theta.append(theta3)
        theta.append(theta4)
        theta.append(theta5)        
        return theta

    def get_position(self, theta, z_axis):
        matrix = np.matmul(self.denavit(theta, 3),self.denavit(theta, 4))

        matrix = np.matmul(self.denavit(theta, 2), matrix)

        matrix = np.matmul(self.denavit(theta, 1), matrix)

        matrix = np.matmul(self.denavit(theta, 0), matrix)
        return self.separate(matrix, z_axis)
    
    def get_orientation(self, alpha, beta, gamma):
        orientation = [[np.cos(alpha)*np.cos(beta), np.cos(alpha)*np.sin(beta)*np.sin(gamma) - np.sin(alpha)*np.cos(gamma), np.cos(alpha)*np.sin(beta)*np.cos(gamma) + np.sin(alpha)*np.sin(gamma) ],
                        [np.sin(alpha)*np.cos(beta), np.sin(alpha)*np.sin(beta)*np.sin(gamma) + np.cos(alpha)*np.cos(gamma), np.sin(alpha)*np.sin(beta)*np.cos(gamma) - np.cos(alpha)*np.sin(gamma) ],
                        [-np.sin(beta), -np.cos(beta)*np.sin(gamma), np.cos(beta)*np.cos(gamma)]]
        return orientation

    def separate(self, matrix, z_axis):
        pos =  np.matmul(matrix, [0,0,z_axis,1])
        rot = []
        for i in range(3):
            rot.append(matrix[i][:-1])
        return pos, np.array(rot)

    def denavit(self, theta, i):
        return  [[np.cos(theta[i]),    -np.sin(theta[i]),  0,   self.a[i]],
            [np.sin(theta[i])*np.cos(self.alpha[i]), np.cos(theta[i])*np.cos(self.alpha[i]), -np.sin(self.alpha[i]), -np.sin(self.alpha[i])*self.d[i]],
            [np.sin(theta[i])*np.sin(self.alpha[i]), np.cos(theta[i])*np.sin(self.alpha[i]), np.cos(self.alpha[i]), np.cos(self.alpha[i])*self.d[i]],
            [0, 0, 0, 1]]

    def fix_quadrante(self, sin, cos):
        if sin >= 0 and cos >= 0:
            return np.arcsin(sin)
        if sin >= 0  and cos <= 0:
            return 3.141592 - np.arcsin(sin)
        if sin <= 0 and cos >= 0:
            return np.arccos(cos) + 3.141592
        if sin <= 0 and cos <= 0:
            return 2*pi - np.arcsin(-sin)