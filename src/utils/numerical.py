import numpy as np

def integration(points):
    dist = 0 
    for i in range(points.shape[0]-1):
        dist+=np.sqrt(np.power(points[i][0] - points[i+1][0], 2)+np.power(points[i][1] - points[i+1][1], 2)+np.power(points[i][2] - points[i+1][2], 2))
    return dist

    
def create_angles(theta_i, theta_f, final_time, steps):
    thetas, omegas, times = [], [], []
    for j in range(5):
        theta, omega, time = [], [], []
        theta.append(theta_i[j])
        omega.append(0)
        time.append(0)
        for i in range(steps-2):
            theta.append((theta_f[j] - theta_i[j])*random.random() + theta_i[j])
            omega.append(random.random())
            time.append(final_time*random.random())
        omega.append(0)
        theta.append(theta_f[j])
        time.append(final_time)
        time.sort()
        if theta_i[j] < theta_f[j]:
            theta.sort()
        else:
            theta.sort(reverse=True)    
        omegas.append(omega)
        thetas.append(theta)
        times.append(time)
    return times, thetas, omegas