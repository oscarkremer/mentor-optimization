import numpy as np

class Mentor:
    def __init__(self):
        self.alpha = [0, -np.pi/2, 0, 0, -np.pi/2]
        self.a = [0, 0, 17.2739, 15.5, 0]
        self.d = [0, 0, 0, 0, 0]
        
    def get_angles(self, pos, rot):
        orientation = rot 
        theta = self._inverse_kinematics(pos, orientation)
        returned_pos, returned_rot = self.get_position(theta)        
        angle3_tag = self.verify(pos, returned_pos)
        if angle3_tag:
            return theta
        else:
            theta = self._inverse_kinematics(pos, orientation, tag=angle3_tag)
            return theta

    def _inverse_kinematics(self, pos, orientation, tag=True):
        theta = []
        theta1 = np.nan_to_num(self.fix_theta1(pos))
        theta.append(theta1)
        theta3 = self.fix_theta3((pos[0]**2+pos[1]**2+pos[2]**2-self.a[2]**2-self.a[3]**2)/(2*self.a[2]*self.a[3]), angle3_tag)
        theta3 = np.nan_to_num(theta3)
        theta2 = -theta3+np.arcsin(((-np.cos(theta3)*self.a[2]-self.a[3])*pos[2]+np.sin(theta3)*self.a[2]*(np.sin(theta1)*pos[1]+pos[0]*np.cos(theta1)))/(np.power(np.cos(theta1)*pos[0]+np.sin(theta1)*pos[1], 2)+pos[2]*pos[2]))
        theta.append(theta2)
        theta.append(theta3)
        sin_theta4 = np.sin(theta2+theta3)*orientation[2][2] - np.cos(theta1)*np.cos(theta2+theta3)*orientation[0][2] - np.sin(theta1)*np.cos(theta2+theta3)*orientation[1][2]
        cos_theta4 = -np.cos(theta2+theta3)*orientation[2][2] - np.cos(theta1)*np.sin(theta2+theta3)*orientation[0][2] - np.sin(theta1)*np.sin(theta2+theta3)*orientation[1][2]
        theta.append(self.fix_quadrante(sin_theta4, cos_theta4))
        sin_theta5 = np.sin(theta1)*orientation[0][0] - np.cos(theta1)*orientation[1][0]
        cos_theta5 = np.sin(theta1)*orientation[0][1] - np.cos(theta1)*orientation[1][1]
        theta.append(self.fix_quadrante(sin_theta5, cos_theta5))
        return theta

    def verify(self, pos, returned_pos):
        diff = pos-returned_pos
        if abs(diff[0])>0.001 or abs(diff[1]>0.001) or abs(diff[2]>0.001):
            return False
        else:
            return True

    def get_position(self, theta, z_axis=0):
        matrix = np.matmul(self.denavit(theta, 3),self.denavit(theta, 4))
        for i in range(3):
            matrix = np.matmul(self.denavit(theta, 2-i), matrix)
        return self.separate(matrix, z_axis)
    
    def get_orientation(self, alpha, beta, gamma):
        return [[np.cos(alpha)*np.cos(beta), np.cos(alpha)*np.sin(beta)*np.sin(gamma) - np.sin(alpha)*np.cos(gamma), np.cos(alpha)*np.sin(beta)*np.cos(gamma) + np.sin(alpha)*np.sin(gamma) ],
                        [np.sin(alpha)*np.cos(beta), np.sin(alpha)*np.sin(beta)*np.sin(gamma) + np.cos(alpha)*np.cos(gamma), np.sin(alpha)*np.sin(beta)*np.cos(gamma) - np.cos(alpha)*np.sin(gamma) ],
                        [-np.sin(beta), -np.cos(beta)*np.sin(gamma), np.cos(beta)*np.cos(gamma)]]

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
            return np.pi - np.arcsin(abs(sin))
        if sin <= 0 and cos >= 0:
            return 2*np.pi - np.arcsin(abs(sin))
        if sin <= 0 and cos <= 0:
            return np.arccos(abs(cos)) + np.pi

    def fix_theta1(self, pos):
        theta = np.arctan(abs(pos[1])/abs(pos[0]))
        if pos[0] >= 0 and pos[1] >= 0:
            return theta
        if pos[0] <= 0 and pos[1] >= 0:
            return np.pi - theta
        if pos[0] <= 0 and pos[1] <= 0:
            return np.pi + theta
        if pos[0] >= 0 and pos[1] <= 0:
            return np.pi - theta

    def fix_theta3(self, cos, tag=True):
        if tag:
            return np.arccos(cos)       
        else:
            return 2*np.pi - np.arccos(cos)    
            