"""
Graph implementation
"""
import numpy as np

class Graph:
    
    """
    · points is a list of letters representing graph points
    · edge_list contains tupes with connected points
    · n_ants is the number of ants participating
    """
    def __init__(self, points, edge_list, n_ants):
        self.points = points
        self.edge_list = edge_list
        self.n_ants = n_ants
        self.ants = []
        self.n_points = len(self.points)
        self.template_matrix = np.zeros((self.n_points, self.n_points), dtype=int)
        self.points_dict = {} 
        self.time = 0
        self.cycle = 0
        
        value = 0
        for i in self.points:
            self.points_dict[i] = value
            value += 1

        self.n_ants_matrix = np.copy(self.template_matrix)
        self.dist_matrix = np.copy(self.template_matrix)
        self.trail_matrix = np.copy(self.template_matrix)
        self.delta_matrix = np.copy(self.template_matrix)
    
    # ants in different points at t = 0
    def initialize_ants(self):
        for ant in self.ants:
            probs = [1/self.n_points for i in range(self.n_points)]
            # uniform distibution for selecting starting point
            ant_start = np.random.choice(self.points, p=probs)
            ant.starting_point = ant_start
            p1 = self.points_dict[ant_start]
            self.n_ants_matrix[p1, p1] += 1

    # initial value c for trail intensity
    def initialize_trail(self):
        c = 0.5
        for edge in self.edge_list:
            p1 = self.points_dict[edge[0]]
            p2 = self.points_dict[edge[1]]

            self.trail_matrix[p1, p2] = c

    # n_ants_point gives the number of ants on a given point
    def n_ants_point(self, point):
        coord = self.points_dict[point]
        return self.n_ants_matrix[coord, coord]
    

    