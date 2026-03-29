"""
Graph implementation
"""
import numpy as np

class Graph:

    # points is a list of letters representing graph points
    # edge_list contains tupes with connected points
    # n_ants is the number of ants participating
    def __init__(self, points, edge_list, n_ants):
        self.point_set = set(points)
        self.edge_list = edge_list
        self.total_ants = n_ants
        self.time = 0
        self.n_points = len(self.point_set)
        self.template_matrix = np.zeros((self.n_points, self.n_points), dtype=int)
        self.points_dict = {}
        
        value = 0
        for i in self.point_set:
            self.points_dict[i] = value
            value += 1

        self.a_matrix = np.copy(self.template_matrix)
        self.n_ants_matrix = np.copy(self.template_matrix)
        self.dist_matrix = np.copy(self.template_matrix)
        self.trail_matrix = np.copy(self.template_matrix)

    # adj_matrix creates the adjacency matrix of the graph
    def adj_matrix(self):
        for connection in self.edge_list:
            p1 = self.points_dict[connection[0]]
            p2 = self.points_dict[connection[1]]
            self.a_matrix[p1, p2] = 1
        
        return self.a_matrix
    
    # n_ants_point gives the number of ants on a given point
    def n_ants_point(self, point):
        coord = self.points_dict[point]
        return self.n_ants_matrix[coord, coord]
    

    



    






