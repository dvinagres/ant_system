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
        self.point_set = set(points)
        self.edge_list = edge_list
        self.total_ants = n_ants
        self.n_points = len(self.point_set)
        self.template_matrix = np.zeros((self.n_points, self.n_points), dtype=int)
        self.points_dict = {} 
        
        value = 0
        for i in self.point_set:
            self.points_dict[i] = value
            value += 1

        self.n_ants_matrix = np.copy(self.template_matrix)
        self.dist_matrix = np.copy(self.template_matrix)
        self.trail_matrix = np.copy(self.template_matrix)
        self.delta_matrix = np.copy(self.template_matrix)
    
    # n_ants_point gives the number of ants on a given point
    def n_ants_point(self, point):
        coord = self.points_dict[point]
        return self.n_ants_matrix[coord, coord]
    

    