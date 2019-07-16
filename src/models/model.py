import itertools
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from functools import partial
from .node.node import Node
from src.utils.numerical import create_angles

class Population:
    def __init__(self, initial, size, generations, p_c, p_m, theta_i, theta_f, time, steps):
        self.size = size
        self.initial = initial
        self.generations = generations
        self.p_c = p_c
        self.p_m = p_m
        self.population_initialization(theta_i, theta_f, time, steps)

    def population_initialization(self, theta_i, theta_f, time, steps):
        self.population = []
        i = 0
        while i < self.initial:
            try:
                element = Node(theta_i, theta_f, time, steps)
                if element.constraint:
                    pass
                else:
                    i+=1
                    print('adding')
                    self.population.append([element.dist, element])
            except:
                pass
            
    def generation(self, theta_i, theta_f, time, steps):
        dataframe = pd.DataFrame()
        angles = pd.DataFrame()
        points = pd.DataFrame()
        best_of_generation = []
        for i in range(self.generations):
            self.population = self.selection(number_bests = self.size)
            best_of_generation.append(self.selection(number_bests = 1)[0][0])

            print(best_of_generation)
            self.analysis()
            members = []
            for member in self.population:
                members.append(member[1])
            combinations = list(itertools.product(members, repeat=2))
            random.shuffle(combinations)
            if self.std < 0.00001:
                for combination in combinations:
                    try:
                        new_element = self.cross_over(combination[0], combination[1], theta_i, theta_f, time, steps)
                        if new_element.constraint:
                            pass
                        else:
                            new_element.dist_calc(steps, theta_i, time)
                            self.population.append([new_element.dist, new_element])
                    except Exception as e:
                        print(e)
                        pass
                    print(len(self.population))
            #    if len(self.population) == self.size:
            #        break
            self.analysis()
            print('Start mutation - {} '.format(i))
            num = 0
            members = []
            for member in self.population:
                members.append(member[1])
            
            for member in members:
                try:
                    num+=1
                    print(num)
                    mutation = self.mutation(member, theta_i, theta_f, time, steps)
                    mutation.test_velocity(time)
                    if mutation.constraint:
                        pass
                    else:
                        mutation.dist_calc(steps, theta_i, time)
                        self.population.append([mutation.dist, mutation])
                except:
                    pass
            print('End mutation - {} '.format(i))

            best_generation = self.selection(number_bests = 1)[0]
            angles_gen = pd.DataFrame()
            points_gen = pd.DataFrame()
            angles_gen['theta1'] = best_generation[1].angle_1
            angles_gen['theta2'] = best_generation[1].angle_2
            angles_gen['theta3'] = best_generation[1].angle_3
            angles_gen['theta4'] = best_generation[1].angle_4
            angles_gen['theta5'] = best_generation[1].angle_5
            x_gen, y_gen, z_gen = [], [], []
            for point in best_generation[1].points:
                x_gen.append(point[0])
                y_gen.append(point[1])
                z_gen.append(point[2])
                
            points_gen['x'] = x_gen
            points_gen['y'] = y_gen
            points_gen['z'] = z_gen
            angles_gen.to_csv('data/angles_{}.csv'.format(i), index=False)
            points_gen.to_csv('data/points_{}.csv'.format(i), index=False)
            
        
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
        if fitness > self.average and (self.maximum-self.average) > 0.00001:
            self.p_c = (self.maximum-fitness)/(self.maximum-self.average)
            self.p_m = (self.maximum-fitness)/(self.maximum-self.average)
        else:
            self.p_c = 0.7
            self.p_m = 0.8
        print(self.p_c)
        print(self.p_m)
        


    def analysis(self):
        fitness = []
        for member in self.population:
            fitness.append(1/member[0])
        self.std = np.std(np.array(fitness))
        self.maximum = max(fitness)
        self.average = sum(fitness)/len(fitness)

    def selection(self, number_bests = 2):
        selected = (sorted(self.population, key = lambda x: float(x[0])))[0:number_bests]
        return selected
   
    def cross_over(self, parent1, parent2, theta_i, theta_f, time, steps):

        self.prob_adaptation(1/(parent1.dist))
        prob_1 = random.random()
        prob_2 = random.random()
        prob_3 = random.random()
        prob_4 = random.random()
        prob_5 = random.random()

        if prob_1 <= self.p_c:
            parent1.joint1 = parent2.joint1
        else:
            pass
        if prob_2 <= self.p_c:
            parent1.joint2 = parent2.joint2
        else:
            pass
        if prob_3 <= self.p_c:
            parent1.joint3 = parent2.joint3
        else:
            pass
        if prob_4 <= self.p_c:
            parent1.joint4 = parent2.joint4
        else:
            pass
        if prob_5 <= self.p_c:
            parent1.joint5 = parent2.joint5
        else:
            pass
        
        return parent1

    def mutation(self, element, theta_i, theta_f, time, steps):
        prob_1 = random.random()
        prob_2 = random.random()
        prob_3 = random.random()
        prob_4 = random.random()
        prob_5 = random.random()
        self.prob_adaptation(1/(element.dist))
        if prob_1 <= self.p_m:
            deltas, delta_thetas, delta_omegas = create_angles(theta_i[0], theta_f[0], time, steps)
            element.joint1 = [deltas, delta_thetas, delta_omegas]
        if prob_2 <= self.p_m:
            deltas, delta_thetas, delta_omegas = create_angles(theta_i[1], theta_f[1], time, steps)
            element.joint2 = [deltas, delta_thetas, delta_omegas]
        if prob_3 <= self.p_m:
            deltas, delta_thetas, delta_omegas = create_angles(theta_i[2], theta_f[2], time, steps)
            element.joint3 = [deltas, delta_thetas, delta_omegas]
        if prob_4 <= self.p_m:
            deltas, delta_thetas, delta_omegas = create_angles(theta_i[3], theta_f[3], time, steps)
            element.joint4 = [deltas, delta_thetas, delta_omegas]
        if prob_5 <= self.p_m:
            deltas, delta_thetas, delta_omegas = create_angles(theta_i[4], theta_f[4], time, steps)
            element.joint5 = [deltas, delta_thetas, delta_omegas]

        return element    
    
        
