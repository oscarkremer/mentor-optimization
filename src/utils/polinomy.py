import numpy as np


class Polinomy:
    def __init__(self, t_i, t_f, theta_i, theta_f, omega_i, omega_f, number=5000):
        self.steps = number
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