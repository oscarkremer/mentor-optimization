import itertools
import multiprocessing
import warnings
import random
import numpy as np
from functools import partial
from multiprocessing import Pool
from .node.node import Node
from src.utils.numerical import create_angles

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
            try:
                element = Node(theta_i, theta_f, time, steps)
                self.population.append([element.dist, element])
            except:
                pass
            
    def generation(self, theta_i, theta_f, time, steps):
        for i in range(self.generations):
            self.population = self.selection(number_bests = 10)
            print(self.population)
            members = []
            for member in self.population:
                members.append(member[1])
            combinations = list(itertools.combinations(members, 2))
            for combination in combinations:
                new_element = self.cross_over(combination[0], combination[1], theta_i, theta_f, time, steps)
                mutation = self.mutation(new_element, theta_i, theta_f, time, steps)
                self.population.append([mutation.dist, mutation])
        

    def selection(self, number_bests = 2):
        selected = (sorted(self.population, key = lambda x: float(x[0])))[0:number_bests]
        return selected
   
    def cross_over(self, parent1, parent2, theta_i, theta_f, time, steps):
        if parent1.dist < parent2.dist:
            pass
        else:
            temp = parent2
            parent2 = parent1
            parent1 = temp

        element = Node(theta_i, theta_f, time, steps)

        if random.random() <= self.p_c:
            element.joint1 = parent1.joint1
        else:
            element.joint1 = parent2.joint1
        if random.random() <= self.p_c:
            element.joint2 = parent1.joint2
        else:
            element.joint2 = parent2.joint2
        if random.random() <= self.p_c:
            element.joint3 = parent1.joint3
        else:
            element.joint3 = parent2.joint3
        if random.random() <= self.p_c:
            element.joint4 = parent1.joint4
        else:
            element.joint4 = parent2.joint4
        if random.random() <= self.p_c:
            element.joint5 = parent1.joint5
        else:
            element.joint5 = parent2.joint5
        element.dist_calc(steps, theta_i, time)
        return element

    def mutation(self, element, theta_i, theta_f, time, steps):
        if random.random() <= self.p_m:
            deltas, delta_thetas, delta_omegas = create_angles(theta_i[0], theta_f[0], time, steps)
            self.joint1 = [deltas, delta_thetas, delta_omegas]
        if random.random() <= self.p_m:
            deltas, delta_thetas, delta_omegas = create_angles(theta_i[1], theta_f[1], time, steps)
            self.joint2 = [deltas, delta_thetas, delta_omegas]
        if random.random() <= self.p_m:
            deltas, delta_thetas, delta_omegas = create_angles(theta_i[2], theta_f[2], time, steps)
            self.joint3 = [deltas, delta_thetas, delta_omegas]
        if random.random() <= self.p_m:
            deltas, delta_thetas, delta_omegas = create_angles(theta_i[3], theta_f[3], time, steps)
            self.joint4 = [deltas, delta_thetas, delta_omegas]
        if random.random() <= self.p_m:
            deltas, delta_thetas, delta_omegas = create_angles(theta_i[4], theta_f[4], time, steps)
            self.joint5 = [deltas, delta_thetas, delta_omegas]
        element.dist_calc(steps, theta_i, time)
        return element    
    
        
