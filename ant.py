"""
Ant implementation
"""
from graph import Graph
import numpy as np

class Ant:

    def __init__(self, id, graph):
        self.id = id
        self.graph = graph
        self.visited_points = set()
        self.starting_point = None 
        self.tour = []  # list of tuples

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

            







        
        


        

