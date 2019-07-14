import itertools
import multiprocessing
import warnings
import random
import numpy as np
from functools import partial
from multiprocessing import Pool
from .node.node import Node
from src.utils import Mentor, Polinomy
from src.utils.numerical import integration, create_angles


class Population:
    def __init__(self, size, generations, p_c, p_m, theta_i, theta_f, time, steps):
        self.size = size
        self.generations = generations
        self.p_c = p_c
        self.p_m = p_m
        self.population_initialization(theta_i, theta_f, time, steps)

    def population_initialization(self, theta_i, theta_f, time, steps):
        self.population = []
        for i in range(self.size):
            self.population.append(Node(theta_i, theta_f, time, steps))
        