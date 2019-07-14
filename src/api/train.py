import itertools
import multiprocessing
import warnings
import random
import math
import numpy as np
from functools import partial
from multiprocessing import Pool
from src.models import Node
from src.utils import Mentor, Polinomy, integration





if __name__=="__main__":
    steps = 10
    time = 2
    theta_i = [0, 0, 0, 0, 0]
    theta_f = [3.1415, 3.1415, 3.1415, 3.1415, 3.1415]
    for i in range(100):
        test = Node(theta_i, theta_f, time, steps)
        print(test.dist)    