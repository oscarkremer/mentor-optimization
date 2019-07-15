import itertools
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from functools import partial
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
        dataframe = pd.DataFrame()
        angles = pd.DataFrame()
        points = pd.DataFrame()
        best_of_generation = []
        for i in range(self.generations):
            self.population = self.selection(number_bests = 5)
            best_of_generation.append(self.selection(number_bests = 1)[0][0])
            print(best_of_generation)
            self.analysis()
            members = []
            for member in self.population:
                members.append(member[1])
            combinations = list(itertools.combinations(members, 2))
            for combination in combinations:
                try:
                    new_element = self.cross_over(combination[0], combination[1], theta_i, theta_f, time, steps)
                    mutation = self.mutation(new_element, theta_i, theta_f, time, steps)
                    self.population.append([mutation.dist, mutation])
                except:
                    pass
        
        dataframe['distance'] = best_of_generation
        best_of_all = self.selection(number_bests = 1)[0]
        angles['theta1'] = best_of_all[1].angle_1
        angles['theta2'] = best_of_all[1].angle_2
        angles['theta3'] = best_of_all[1].angle_3
        angles['theta4'] = best_of_all[1].angle_4
        angles['theta5'] = best_of_all[1].angle_5
        x, y, z = [], [], []
        for point in best_of_all[1].points:
            x.append(point[0])
            y.append(point[1])
            z.append(point[2])
            
        points['x'] = x
        points['y'] = y
        points['z'] = z
        angles.to_csv('data/angles.csv', index=False)
        points.to_csv('data/points.csv', index=False)
        dataframe.to_csv('data/results.csv', index=False)



    def prob_adaptation(self, fitness):
        if fitness > self.average:
            self.p_c = (self.maximum-fitness)/(self.maximum-self.average)
            self.p_m = 0.4*(self.maximum-fitness)/(self.maximum-self.average)
            print(self.p_c)
            print(self.p_m)
        else:
            self.p_c = 0.7
            self.p_m = 0.05
            print(self.p_c)
            print(self.p_m)
            

    def analysis(self):
        fitness = []
        for member in self.population:
            fitness.append(1/member[0])
        self.maximum = max(fitness)
        self.average = sum(fitness)/len(fitness)

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
        self.prob_adaptation(1/(parent1.dist))
        element = Node(theta_i, theta_f, time, steps)
        
        if random.random() <= self.p_c:
            joint_prob = random.random()
            if joint_prob <= 0.2 and joint_prob > 0:
                element.joint1 = parent2.joint1
            if joint_prob <= 0.4 and joint_prob > 0.2:
                element.joint2 = parent2.joint2
            if joint_prob <= 0.6 and joint_prob > 0.4:
                element.joint3 = parent2.joint3
            if joint_prob <= 0.8 and joint_prob > 0.6:
                element.joint4 = parent2.joint4
            if joint_prob <= 1 and joint_prob > 0.8:
                element.joint5 = parent2.joint5
        else:
            element.joint1 = parent1.joint1
            element.joint2 = parent1.joint2
            element.joint3 = parent1.joint3
            element.joint4 = parent1.joint4
            element.joint5 = parent1.joint5
        element.dist_calc(steps, theta_i, time)
        return element

    def mutation(self, element, theta_i, theta_f, time, steps):
        if random.random() <= self.p_m:
            joint_prob = random.random()
            if joint_prob < 0.2 and joint_prob > 0:
                deltas, delta_thetas, delta_omegas = create_angles(theta_i[0], theta_f[0], time, steps)
                self.joint1 = [deltas, delta_thetas, delta_omegas]
            if joint_prob < 0.4 and joint_prob > 0.3:
                deltas, delta_thetas, delta_omegas = create_angles(theta_i[1], theta_f[1], time, steps)
                self.joint2 = [deltas, delta_thetas, delta_omegas]
            if joint_prob < 0.6 and joint_prob  > 0.4:
                deltas, delta_thetas, delta_omegas = create_angles(theta_i[2], theta_f[2], time, steps)
                self.joint3 = [deltas, delta_thetas, delta_omegas]
            if joint_prob < 0.8 and joint_prob > 0.6:
                deltas, delta_thetas, delta_omegas = create_angles(theta_i[3], theta_f[3], time, steps)
                self.joint4 = [deltas, delta_thetas, delta_omegas]
            if joint_prob < 1 and joint_prob > 0.8:
                deltas, delta_thetas, delta_omegas = create_angles(theta_i[4], theta_f[4], time, steps)
                self.joint5 = [deltas, delta_thetas, delta_omegas]

        element.dist_calc(steps, theta_i, time)
        return element    
    
        
