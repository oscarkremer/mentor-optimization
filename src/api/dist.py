import numpy as np 
from src.utils import Mentor


class polinomy:
    def __init__(self, t_i, t_f, theta_i, theta_f, omega_i, omega_f, number=10000):
        self.t_i = t_i
        self.t_f = t_f
        self.theta_i = theta_i
        self.theta_f = theta_f
        self.omega_i = omega_i
        self.omega_f = omega_f
        self.generate_points(number=number)

    def generate_coeff(self):
        times = [[1, self.t_i, np.power(self.t_i, 2), np.power(self.t_i, 3)],
            [1, self.t_f, np.power(self.t_f, 2), np.power(self.t_f, 3)],
            [0,  1,  2*self.t_i,  3*np.power(self.t_i, 2)],
            [0,  1,  2*self.t_f,   3*np.power(self.t_f,2)]]
        coef = np.matmul(np.linalg.inv(times),np.array([[self.theta_i],[self.theta_f],[self.omega_i],[self.omega_f]]))
        self.coef = coef.reshape((coef.shape[0]))
        self.a_0 = coef[0][0]
        self.a_1 = coef[1][0]
        self.a_2 = coef[2][0]
        self.a_3 = coef[3][0]
      
    def generate_points(self, number):
        points = np.linspace(self.t_i, self.t_f, number)
        self.generate_coeff()
        self.thetas = self.a_0 + self.a_1*(np.power(points, 1)) + self.a_2*np.power(points, 2) + self.a_3*np.power(points,3) 
        self.delta_thetas = self.a_1 + 2*self.a_2*np.power(points,1) + 3*self.a_3*np.power(points, 2)



if __name__ == '__main__':

    theta1_i, theta1_f = 0, 3.141592
    omega1_i, omega1_f = 0, 0
    t_i = 0
    t_f = 2
    
    theta2_i, theta2_f = 0, 3.141592
    omega2_i, omega2_f = 0, 0
    t_i = 0
    t_f = 2
    
    theta3_i, theta3_f = 0, 3.141592
    omega3_i, omega3_f = 0, 0
    t_i = 0
    t_f = 2
    
    theta4_i, theta4_f = 0, 3.141592
    omega4_i, omega4_f = 0, 0
    t_i = 0
    t_f = 2
    
    theta5_i, theta5_f = 0, 3.141592
    omega5_i, omega5_f = 0, 0
    t_i = 0
    t_f = 2
    
    poly_1 = polinomy(t_i, t_f, theta1_i, theta1_f, omega1_i, omega1_f)
    poly_2 = polinomy(t_i, t_f, theta1_i, theta1_f, omega1_i, omega1_f)
    poly_3 = polinomy(t_i, t_f, theta1_i, theta1_f, omega1_i, omega1_f)
    poly_4 = polinomy(t_i, t_f, theta1_i, theta1_f, omega1_i, omega1_f)
    poly_5 = polinomy(t_i, t_f, theta1_i, theta1_f, omega1_i, omega1_f)
    mentor = Mentor()
    dist_4, dist_3, dist_2, dist_1 = 0, 0, 0, 0

    for i in range(10000):
        dist_4+=6*poly_4.delta_thetas[i]*(2/10000)

    for i in range(10000):
        dist_3+=poly_3.delta_thetas[i]*np.sqrt(36 - 12*mentor.a[3]*np.sin(poly_4.thetas[i])+ np.power(mentor.a[3], 2))*(2/10000)

    for i in range(10000):
        dist_2+=poly_2.delta_thetas[i]*np.sqrt(36+np.power(mentor.a[2], 2)+np.power(mentor.a[3], 2)+2*mentor.a[2]*mentor.a[3]*np.cos(poly_3.thetas[i])-12*mentor.a[2]*np.sin(poly_4.thetas[i] + poly_3.thetas[i])
        -12*mentor.a[3]*np.sin(poly_4.thetas[i]))*(2/10000)

    for i in range(10000):
        dist_1+=poly_1.delta_thetas[i]*np.sqrt(np.power(mentor.a[2]*np.cos(poly_2.thetas[i]) + 
        mentor.a[3]*np.cos(poly_2.thetas[i] + poly_3.thetas[i]) - 
        6*np.sin(poly_2.thetas[i]+poly_3.thetas[i]+poly_4.thetas[i]), 2))*(2/10000)

    print(dist_4)
    print(dist_3)
    print(dist_2)
    print(dist_1)


    

