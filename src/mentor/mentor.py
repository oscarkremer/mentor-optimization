'''
This script defines the Mentor class package, where there are
specified as Mentor methods the computations of direct and
inverse kinematics

This package can be imported with:
from src.mentor import Mentor
'''
import itertools
import numpy as np

class Mentor:
    '''
    Mentor Class. This class represents the mentor didactic robot, obeying 
    the laws of direct and inverse kinematics, and any physical constraint
    of movement, both angulars position or velocity. 

    Attributes
    ----------
    alpha : list
        Angle list of Denavit Hartenberg parameter.
    a: list
        List of perpendicular distance between joints.
    d: list
        List of perpendicular distance between links.
    
    Methods
    -------
    test_inverse_kinematics(self, pos, rot, tag_theta1=True, tag_theta2=True, tag_theta3=True):  
        Method to test with a certain set of condition represents a possible situation for the robot.
    get_angles(self, pos, rot):
        Method to test with all possible scenarious of angles.
    _inverse_kinematics(self, pos, orientation, tag_theta1=True, tag_theta2=True, tag_theta3=True):
        Angles computation in inverse kinematics.
    verify(self, pos, rot, returned_pos, returned_rot):
        Verification if computed position is equal to desired position.
    get_position(self, theta, z_axis=0):
        Method to apply direct kinematics 
    get_orientation(self, alpha, beta, gamma):
        Method to get end effector orientation consideration Alpha, Beta and
        Gamma - XYZ angles.
    separate(self, matrix, z_axis):
        Method to separate a 4x4 matrix in rotational matrix and position array.
    denavit(self, theta, i):
        Method to apply the Denavit-Hartenberg to find the transformation matrix.
    fix_quadrante(self, sin, cos):
        Method to adjust the angle quadrant from its sine and cosine.
    fix_theta(self, param, tag, angle):
        Method to adjust the angle quadrant from any possible set o parameters.
    '''
    def __init__(self):
        '''
        The constructor method doesn't use any parameters. 
        This method is only responsible to define the Denavit-Hartenberg 
        parameters as Mentor attributes.
        '''
        self.alpha = [0, -np.pi/2, 0, 0, -np.pi/2]
        self.a = [0, 0, 17.2739, 15.5, 0]
        self.d = [0, 0, 0, 0, 0]

    def test_inverse_kinematics(self, pos, rot, tag_theta1=True, tag_theta2=True, tag_theta3=True):  
        '''
        Method to test with a certain set of condition represents a possible situation for the robot.

        Parameters
        ----------
        pos: list
            List with position in the cartesian space of the end effector grip.
        rot: list
            Rotation matrix of the end effector grip.
        tag_theta1: bool(optional):
            Tag to identify error in theta-1
        tag_theta2: bool(optional):
            Tag to identify error in theta-2
        tag_theta3: bool(optional):
            Tag to identify error in theta-3
 
        Returns
        -------
        tag:
            Verification if there was any error in inverse kinematics.
        theta:
            List containing the joint angles encountered.
        '''

        theta = self._inverse_kinematics(pos, rot, tag_theta1=tag_theta1, tag_theta2=tag_theta2, tag_theta3=tag_theta3)
        returned_pos, returned_rot = self.get_position(theta)        
        tag = self.verify(pos, rot, returned_pos, returned_rot)
        return tag, theta

    def get_angles(self, pos, rot):
        '''
        Method to test with all possible scenarious of angles.

        Parameters
        ----------
        pos: list
            List with position in the cartesian space of the end effector grip.
        rot: list
            Rotation matrix of the end effector grip.

        Returns
        -------
        tag:
            Tag that identifies if position is or isn't possible.
        theta:
            List of joint angles returned in case position/orientation is possible.
        '''
        for element in itertools.product([True, False],[False, True],[False, True]):
            tag, theta = self.test_inverse_kinematics(pos, rot, element[0], element[1], element[2])
            if tag:
                return False, theta
        return True, theta 

    def _inverse_kinematics(self, pos, orientation, tag_theta1=True, tag_theta2=True, tag_theta3=True):
        '''
        Angles computation in inverse kinematics.

        Parameters
        ----------
        pos: list
            List with position in the cartesian space of the end effector grip.
        rot: list
            Rotation matrix of the end effector grip.
        tag_theta1: bool(optional):
            Tag to identify error in theta-1.
        tag_theta2: bool(optional):
            Tag to identify error in theta-2.
        tag_theta3: bool(optional):
            Tag to identify error in theta-3.
         
        Returns
        -------
        theta:
            List of joint angles returned in case position/orientation is possible.
        '''
        theta = []
        theta1 = np.nan_to_num(self.fix_theta(pos, tag_theta1, 'theta1'))
        theta.append(theta1)
        theta3 = self.fix_theta((pos[0]**2+pos[1]**2+pos[2]**2-self.a[2]**2-self.a[3]**2)/(2*self.a[2]*self.a[3]), tag_theta3, 'theta3')
        theta3 = np.nan_to_num(theta3)
        theta2  = np.nan_to_num(-theta3+self.fix_theta(((-np.cos(theta3)*self.a[2]-self.a[3])*pos[2]+np.sin(theta3)*self.a[2]*(np.sin(theta1)*pos[1]+pos[0]*np.cos(theta1)))/(np.power(np.cos(theta1)*pos[0]+np.sin(theta1)*pos[1], 2)+pos[2]*pos[2]), tag_theta2, 'theta2'))
        theta.append(theta2)
        theta.append(theta3)
        sin_theta4 = np.sin(theta2+theta3)*orientation[2][2] - np.cos(theta1)*np.cos(theta2+theta3)*orientation[0][2] - np.sin(theta1)*np.cos(theta2+theta3)*orientation[1][2]
        cos_theta4 = -np.cos(theta2+theta3)*orientation[2][2] - np.cos(theta1)*np.sin(theta2+theta3)*orientation[0][2] - np.sin(theta1)*np.sin(theta2+theta3)*orientation[1][2]
        theta.append(self.fix_quadrante(sin_theta4, cos_theta4))
        sin_theta5 = np.sin(theta1)*orientation[0][0] - np.cos(theta1)*orientation[1][0]
        cos_theta5 = np.sin(theta1)*orientation[0][1] - np.cos(theta1)*orientation[1][1]
        theta.append(self.fix_quadrante(sin_theta5, cos_theta5))
        return theta

    def verify(self, pos, rot, returned_pos, returned_rot):
        '''
        This method executes verification if computed position is equal to desired position.

        Parameters
        ----------
        pos: list
            List with position in the cartesian space of the end effector grip.
        rot: list
            Rotation matrix of the end effector grip.
        returned_pos: list
            Lista com informações de posição do atuador final do manipuldor 
            no espaço cartesiano.
        returned_rot: list
            Matriz de rotação do atuador final do manipulador no espaço 
            cartesiano.
        
        Retorna
        -------
        Retorna boolean para identifição se a posição está ou não correta.
        '''
        diff = pos[:3]-returned_pos[:3]
        rot_norm = np.linalg.norm(rot-returned_rot)
        if rot_norm > 0.001 or abs(diff[0])>0.001 or abs(diff[1]>0.001) or abs(diff[2]>0.001):
            return False
        else:
            return True

    def get_position(self, theta, z_axis=0):
        '''
        Method to apply direct kinematics in a set of inputed joint angles.

        Parameters
        ----------
        theta: Numpy Array
            Vetor com os ângulos das juntas.
        z_axis: float (opcional)
            Distância do sistema de coordenadas do atuador final em 
            relação à última junta rotacional do Mentor.

        Retorna
        -------
        Matrizes de rotação e orientação que definem o sistema de coordenada
        final do atuador no sistema cartesiano da base.
        '''
        matrix = np.matmul(self.denavit(theta, 3),self.denavit(theta, 4))
        for i in range(3):
            matrix = np.matmul(self.denavit(theta, 2-i), matrix)
        return self.separate(matrix, z_axis)
    
    def get_orientation(self, alpha, beta, gamma):
        '''
        Method to get end effector orientation consideration Alpha, Beta and
        Gamma - XYZ angles.

        Parameters
        ----------
        alpha: float
            Orientation angle of X axis.
        beta: float
            Orientation angle of Y axis.
        gamma: float
            Orientation angle of Z axis.

        Returns
        -------
        Matriz de rotação encontrada a partir dos ângulos alpha-beta-gamma.
        '''
        return [[np.cos(alpha)*np.cos(beta), np.cos(alpha)*np.sin(beta)*np.sin(gamma) - np.sin(alpha)*np.cos(gamma), np.cos(alpha)*np.sin(beta)*np.cos(gamma) + np.sin(alpha)*np.sin(gamma) ],
                        [np.sin(alpha)*np.cos(beta), np.sin(alpha)*np.sin(beta)*np.sin(gamma) + np.cos(alpha)*np.cos(gamma), np.sin(alpha)*np.sin(beta)*np.cos(gamma) - np.cos(alpha)*np.sin(gamma) ],
                        [-np.sin(beta), -np.cos(beta)*np.sin(gamma), np.cos(beta)*np.cos(gamma)]]

    def separate(self, matrix, z_axis):
        '''
        Method to separate a 4x4 matrix in rotational matrix and position array.

        Parameters
        ----------
        Matrix: Numpy Array
            Joint angle 4x4 matrix.
        z_axis: float (opcional)
            Distance in Z Axis to define an extra frame.

        Returns
        -------
        pos: float
            3x1 Array that defined the position of end effector grip.
        np.array(rot):
            3x3 Matrix that defines the orientation of end effector grip.
        '''
        pos =  np.matmul(matrix, [0,0,z_axis,1])
        rot = [matrix[i][:-1] for i in range(3)]
        return pos, np.array(rot)

    def denavit(self, theta, i):
        '''
        Method to apply the Denavit-Hartenberg to find the transformation matrix.

        Parameters
        ----------
        theta: list
            Lista com ângulos das juntas em determinado instante.
        i: int
            Index que definirá entre quais sistemas coordenados está acontecendo 
            está transformação de coordenadas.

        Returns
        -------
        Matrix 4x4 extendida e triangular por blocos que contém 
            matriz de rotação (3x3) e vetor de posição (3x1).
        '''
        return  [[np.cos(theta[i]), -np.sin(theta[i]),  0,   self.a[i]],
            [np.sin(theta[i])*np.cos(self.alpha[i]), np.cos(theta[i])*np.cos(self.alpha[i]), -np.sin(self.alpha[i]), -np.sin(self.alpha[i])*self.d[i]],
            [np.sin(theta[i])*np.sin(self.alpha[i]), np.cos(theta[i])*np.sin(self.alpha[i]), np.cos(self.alpha[i]), np.cos(self.alpha[i])*self.d[i]],
            [0, 0, 0, 1]]

    def fix_quadrante(self, sin, cos):
        '''
        Method to adjust the angle quadrant from its sine and cosine.

        Parameters
        ----------
        sin: float
            Angle sine.
        cos: float
            Angle cossine.
        
        Returns
        -------
        Angle adjusted to the right quadrant.
        '''
        if sin >= 0 and cos >= 0:
            return np.arcsin(abs(sin))
        if sin >= 0  and cos <= 0:
            return np.pi - np.arcsin(abs(sin))
        if sin <= 0 and cos >= 0:
            return 2*np.pi - np.arcsin(abs(sin))
        if sin <= 0 and cos <= 0:
            return np.arccos(abs(cos)) + np.pi

    def fix_theta(self, param, tag, angle):
        '''
        Method to adjust the angle quadrant in a more generic way.

        Parameters
        ----------
        param: float
            Used parameter to identify if the angle is correct. Param can be
            a list of (x, y), sine or cossine.
        tag: boolean
            Tag that identifies if any error have already been detected.
        angle: str
            Specific angle analysed.
            
        Returns
        -------
        Angle adjusted to the right quadrant.
        '''
        if angle=='theta1':
            if abs(param[0]) < 0.001:  
                param = np.pi/2
            else:
                param = np.arctan(param[1]/ param[0])
        if tag and param>=0:
            if angle == 'theta1':
                return param
            if angle == 'theta2':
                return np.arcsin(abs(param))       
            if angle == 'theta3':
                return np.arccos(abs(param))       
        if not tag and param>=0:
            if angle == 'theta1':
                return np.pi + param
            if angle == 'theta2':
                return np.pi-np.arcsin(abs(param))
            if angle == 'theta3':
                return 2*np.pi-np.arccos(abs(param))   
        if tag and param<=0:
            if angle == 'theta1':
                return 2*np.pi - abs(param)
            if angle == 'theta2':
                return 2*np.pi - np.arcsin(abs(param))
            if angle == 'theta3':   
                return np.pi-np.arccos(abs(param))       
        if not tag and param<=0:
            if angle == 'theta1':
                return np.pi - abs(param)
            if angle == 'theta2':
                return np.pi + np.arcsin(abs(param))
            if angle == 'theta3':
                return np.pi + np.arccos(abs(param))