import numpy as np 


if __name__ == '__main__':

    theta_1, theta_2 = 0, 3.141592
    omega_1, omega_2 = 0, 0
    t_1 = 0
    t_2 = 2
    times = [[1, t_1, t_1*t_1, t_1*t_1*t_1],
            [1, t_2, t_2*t_2, t_2*t_2*t_2],
            [0,  1,  2*t_1,  3*t_1*t_1],
            [0,  1,  2*t_2,   3*t_2*t_2]]

    print(np.linalg.inv(times))
    print(np.matmul(np.linalg.inv(times),np.array([[1],[1],[1],[1]])))