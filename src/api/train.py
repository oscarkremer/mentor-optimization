import itertools
import multiprocessing
import warnings
import random
import math
import numpy as np
from functools import partial
from multiprocessing import Pool
from src.models import Population
from src.utils import Mentor, Polinomy, integration



if __name__=="__main__":
    steps = 10
    time = 5
    robot = Mentor()
    pos = np.zeros(3)
    angles = np.zeros(3)
    pos[0] = input('X 1 ')
    pos[1] = input('Y 1')
    pos[2] = input('Z 1')
    angles[0] = input('alpha i ')
    angles[1] = input('beta i ')
    angles[2] = input('gamma i ')
    angles[0] = 3.141592*angles[0]/180
    angles[1] = 3.141592*angles[1]/180
    angles[2] = 3.141592*angles[2]/180
    
    theta_i = robot.get_angles(pos,angles)

    pos[0] = input('X f ')
    pos[1] = input('Y f')
    pos[2] = input('Z F')
    angles[0] = input('alpha f ')
    angles[1] = input('beta f ')
    angles[2] = input('gamma f ')
    angles[0] = 3.141592*angles[0]/180
    angles[1] = 3.141592*angles[1]/180
    angles[2] = 3.141592*angles[2]/180
    
    theta_f = robot.get_angles(pos,angles)


    #theta_i = [0, 0, 0, 0, 0]
#   theta_f = [3.1415, 3.1415/6, 3.1415/6, 3.1415/2, 3.1415/2]
    test = Population(30, 20, 0.7, 0.4, theta_i, theta_f, time, steps)
    test.generation(theta_i, theta_f, time, steps)
        