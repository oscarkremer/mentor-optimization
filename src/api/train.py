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
    time = 2
    theta_i = [0, 0, 0, 0, 0]
    theta_f = [3.1415, 3.1415, 3.1415, 3.1415, 3.1415]
    test = Population(10, 3, 0.9, 0.05, theta_i, theta_f, time, steps)
        