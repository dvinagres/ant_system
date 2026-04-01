"""
Ant implementation
"""
from graph import Graph
import numpy as np

class Ant:

    def __init__(self, id):
        self.id = id
        self.time = 0
        self.visited_points = set()
        self.graph = Graph(0, [], 0)
        self.starting_point = self.graph.points_dict[0] # Default start
        self.tour = []
        self.trail_intensity = 0.03 # trail intensity at time 0 
        self.cycle = 1
        self.iteration = 1
        self.rho = 0.5  # < 1 to avoid unlimited accumulation of trail
        self.q = 0.3

    """
    update_time
    "An ITERATION of the AS algorithm is the m moves carried out by the m ants in the interval (t, t+1)"
    "Every n interations -CYCLE- each ant has completed a tour"
    """
    def update_time(self):
        if self.iteration == self.graph.total_ants:
            self.time += 1

    # tour_completed confirms if an ant has made a tour
    def tour_completed(self, next_point):
        completed = False
        if len(self.visited_points) == self.graph.n_points and next_point == self.starting_point:
            completed = True
        return completed
    
    """
    · if tour completed, update_intensity on edge (i, j)
    · if it's completed, delta_quantity of the kth ant = q -constant- / L -tour length of the kth ant-
    """
    def update_intensity(self, tour):
        tour_length = len(tour)
        delta_quantity = self.q / tour_length
        delta_sum = 0

        for i in range(1, self.iteration):
            delta_sum += delta_quantity

        # New intensity for t + n
        self.trail_intensity = self.rho * self.trail_intensity + delta_sum

    

        
        


        

