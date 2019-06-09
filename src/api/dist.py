import numpy as np 

class polinomy:
    def __init__(self, t_i, t_f, theta_i, theta_f, omega_i, omega_f):
        self.t_i = t_i
        self.t_f = t_f
        self.theta_i = theta_i
        self.theta_f = theta_f
        self.omega_i = omega_i
        self.omega_f = omega_f
        self.generate_points(, points=1000)


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
      
    def generate_points(self, points=1000):
        points = np.linspace(t_i, t_f, 1000)
        self.generate_coeff()
        self.thetas = self.a_0 + self.a_1*(np.power(points, 1)) + self.a_2*np.power(points, 2) + self.a_3*np.power(points,3) 

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
    
    poly = polinomy(t_i, t_f, theta1_i, theta1_f, omega1_i, omega1_f)
    poly.generate_points()
