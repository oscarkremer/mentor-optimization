import numpy as np

class Mentor:
    def __init__(self):
        self.alpha = [0, -np.pi/2, 0, 0, -np.pi/2]
        self.a = [0, 0, 17.2739, 15.5, 0]
        self.d = [0, 0, 0, 0, 0]
        
    def get_angles(self, pos, angles):
        orientation = angles
        theta = []
        theta1 = np.arctan(pos[1]/pos[0])
        theta3 = np.arccos((pos[0]**2 + pos[1]**2 + pos[2]**2 - self.a[2]**2 - self.a[3]**2)/(2*self.a[2]*self.a[3]))
        theta2 = -theta3 + np.arcsin(((-np.cos(theta3)*self.a[2] - self.a[3])*pos[2] + np.sin(theta3)*self.a[2]*(np.sin(theta1)*pos[1]+pos[0]*np.cos(theta1)))/(np.power(np.cos(theta1)*pos[0]+np.sin(theta1)*pos[1], 2)+ pos[2]*pos[2]))
        theta4 = np.arcsin(np.sin(theta2+theta3)*orientation[2][2] - np.cos(theta1)*np.cos(theta2+theta3)*orientation[0][2] - np.sin(theta1)*np.cos(theta2+theta3)*orientation[1][2])
        theta5 = np.arcsin(np.sin(theta1)*orientation[0][0] - np.cos(theta1)*orientation[1][0])
        theta.append(theta1)
        theta.append(theta2)
        theta.append(theta3)
        theta.append(theta4)
        theta.append(theta5)        
        return theta

    def get_position(self, theta):
        matrix = np.identity(4)
        for i in range(5):
            matrix = np.matmul(matrix, self.denavit(theta, i))
        return self.separate(matrix)
    
    def get_orientation(self, alpha, beta, gamma):
        orientation = [[np.cos(alpha)*np.cos(beta), np.cos(alpha)*np.sin(beta)*np.sin(gamma) - np.sin(alpha)*np.cos(gamma), np.cos(alpha)*np.sin(beta)*np.cos(gamma) + np.sin(alpha)*np.sin(gamma) ],
                        [np.sin(alpha)*np.cos(beta), np.sin(alpha)*np.sin(beta)*np.sin(gamma) + np.sin(alpha)*np.cos(gamma), np.sin(alpha)*np.sin(beta)*np.cos(gamma) + np.cos(alpha)*np.sin(gamma) ],
                        [-np.sin(beta), -np.cos(beta)*np.sin(gamma), np.cos(beta)*np.cos(gamma)]]
        return orientation

    def separate(self, matrix):
        pos =  np.matmul(matrix, [0,0,0,1])
        rot = []
        for i in range(3):
            rot.append(matrix[i][:-1])
        return pos, np.array(rot)

    def denavit(self, theta, i):
        return  [[np.cos(theta[i]),    -np.sin(theta[i]),  0,   self.a[i]],
            [np.sin(theta[i])*np.cos(self.alpha[i]), np.cos(theta[i])*np.cos(self.alpha[i]), -np.sin(self.alpha[i]), -np.sin(self.alpha[i])*self.d[i]],
            [np.sin(theta[i])*np.sin(self.alpha[i]), np.cos(theta[i])*np.sin(self.alpha[i]), np.cos(self.alpha[i]), np.cos(self.alpha[i])*self.d[i]],
            [0, 0, 0, 1]]

