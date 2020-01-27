import itertools
import random
import numpy as np
import pandas as pd
from .node.node import Node
from src.utils.numerical import create_angles, integration

class Population:
    def __init__(self, initial, size, generations, p_c, p_m, theta_i, theta_f, time, steps, points):
        self.size = size
        self.initial = initial
        self.generations = generations
        self.p_c = p_c
        self.p_m = p_m
        self.points = points

    def initialization(self, theta_i, theta_f, time, steps):
        population = []
        i = 0
        print('Population - First Generation Initilization')
        while i < self.initial:
            element = Node(theta_i, theta_f, time, steps, self.points)
            element.find_points(theta_i, time, steps)
            if not element.constraint:
                i+=1
                metric = integration(np.array(element.points))
                population.append([metric, element])
        return population
    
    def generation(self, population,  theta_i, theta_f, time, steps):
        best_of_generation = []
        for i in range(self.generations):
            population = self.selection(population, number_bests = self.size)
            actual_best = self.selection(population, number_bests = 1)[0][0]
            self.analysis(population)
            print('Start Cross Over - {} '.format(i))
            members = []
            for member in population:
                members.append(member[1])
            combinations = list(itertools.product(members, repeat=2))
            for combination in combinations:
                try:
                    new_element = self.cross_over(combination, theta_i, theta_f, time, steps)
                    new_element.find_points(theta_i, time, steps)
                    if not new_element.constraint:
                        metric = integration(np.array(new_element.points))
                        population.insert(len(population), [metric, new_element]) 
                except Exception as e:
                    pass
            self.analysis(population)
            print('Start mutation - {} '.format(i))
            for member in members:
                try:
                    mutation = self.mutation(member, theta_i, theta_f, time, steps)
                    mutation.find_points(theta_i, time, steps)
                    if not mutation.constraint:
                        metric = integration(np.array(mutation.points))
                        population.append([metric, mutation])
                except Exception as e:
                    pass
            best_of_generation.append(self.selection(population, number_bests = 1)[0][0])
            best_generation = self.selection(population, number_bests = 1)[0]
        best_of_all = self.selection(population, number_bests = 1)[0]
        self.save_csv(population, actual_best, best_of_all)


    def save_csv(self, population, actual_best, best_of_all):
        dataframe = pd.DataFrame()
        angles = pd.DataFrame()
        points = pd.DataFrame()
        dataframe['distance'] = actual_best
        best_of_all = self.selection(population, number_bests = 1)[0]
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
        angles.to_csv('data/processed/angles.csv', index=False)
        points.to_csv('data/processed/points.csv', index=False)
        dataframe.to_csv('data/processed/results.csv', index=False)


    def prob_adaptation(self, fitness):
        if fitness > self.average and (self.maximum-self.average) > 0.00001:
            self.p_c = (self.maximum-fitness)/(self.maximum-self.average)
            self.p_m = (self.maximum-fitness)/(self.maximum-self.average)
        else:
            self.p_c = 0.7
            self.p_m = 0.8

    def analysis(self, population):
        fitness = []
        for member in population:
            fitness.append(1/member[0])
        self.std = np.std(np.array(fitness))
        self.maximum = max(fitness)
        self.average = sum(fitness)/len(fitness)

    def selection(self, population, number_bests = 2):
        return (sorted(population, key = getitem))[0:number_bests]
   
    def cross_over(self, parents, theta_i, theta_f, time, steps):
        self.prob_adaptation(1/integration(np.array(parents[0].points)))
        if random.random() <= self.p_c:
            parents[0].joint1 = parents[1].joint1
        if random.random() <= self.p_c:
            parents[0].joint2 = parents[1].joint2
        if random.random() <= self.p_c:
            parents[0].joint3 = parents[1].joint3
        if random.random() <= self.p_c:
            parents[0].joint4 = parents[1].joint4
        if random.random() <= self.p_c:
            parents[0].joint5 = parents[1].joint5
        return parents[0]

    def mutation(self, member, theta_i, theta_f, time, steps):
        element = Node(theta_i, theta_f, time, steps, self.points)
        element.joint1 = member[1].joint1
        element.joint2 = member[1].joint2
        element.joint3 = member[1].joint3
        element.joint4 = member[1].joint4
        element.joint5 = member[1].joint5
        self.prob_adaptation(1/member[0])
        if random.random() <= self.p_m:
            deltas, delta_thetas, delta_omegas = create_angles(theta_i[0], theta_f[0], time, steps)
            element.joint1 = [deltas, delta_thetas, delta_omegas]
        if random.random() <= self.p_m:
            deltas, delta_thetas, delta_omegas = create_angles(theta_i[1], theta_f[1], time, steps)
            element.joint2 = [deltas, delta_thetas, delta_omegas]
        if random.random() <= self.p_m:
            deltas, delta_thetas, delta_omegas = create_angles(theta_i[2], theta_f[2], time, steps)
            element.joint3 = [deltas, delta_thetas, delta_omegas]
        if random.random() <= self.p_m:
            deltas, delta_thetas, delta_omegas = create_angles(theta_i[3], theta_f[3], time, steps)
            element.joint4 = [deltas, delta_thetas, delta_omegas]
        if random.random() <= self.p_m:
            deltas, delta_thetas, delta_omegas = create_angles(theta_i[4], theta_f[4], time, steps)
            element.joint5 = [deltas, delta_thetas, delta_omegas]
        return element    

def getitem(item):
    return item[0]