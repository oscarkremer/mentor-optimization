import random
import numpy as np

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


        