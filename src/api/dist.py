import numpy as np 
from src.utils import Mentor, Polinomy

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
    
    poly_1 = Polinomy(t_i, t_f, theta1_i, theta1_f, omega1_i, omega1_f)
    poly_2 = Polinomy(t_i, t_f, theta1_i, theta1_f, omega1_i, omega1_f)
    poly_3 = Polinomy(t_i, t_f, theta1_i, theta1_f, omega1_i, omega1_f)
    poly_4 = Polinomy(t_i, t_f, theta1_i, theta1_f, omega1_i, omega1_f)
    poly_5 = Polinomy(t_i, t_f, theta1_i, theta1_f, omega1_i, omega1_f)
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

    print(dist_4+dist_3+dist_2+dist_1)


    

