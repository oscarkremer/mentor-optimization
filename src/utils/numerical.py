import random
import numpy as np

def integration(points):
    dist = 0 
    for i in range(points.shape[0]-1):
        dist+=np.sqrt((points[i][0] - points[i+1][0])**2 + (points[i][1] - points[i+1][1])**2 + (points[i][2] - points[i+1][2])**2)
    return dist

def create_angles(theta_i, theta_f, final_time, steps):
    theta, omega, time = [theta_i], [0], [0]
    for i in range(steps-2):
        theta.append((theta_f - theta_i)*random.random() + theta_i)
        omega.append(5*random.random())
        time.append(final_time*random.random())
    omega.append(0)
    theta.append(theta_f)
    time.append(final_time)
    time.sort()
    if theta_i < theta_f:
        theta.sort()
    else:
        theta.sort(reverse=True)
    return time, theta, omega


        