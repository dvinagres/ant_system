"""
AS implementation
"""

import numpy as np

class Algorithm:

    def __init__(self, graph, ants):
        self.graph = graph
        self.ants = ants
        self.time = 0
        self.cycle = 1
        self.iteration = 1
        self.cycle = 1
        self.iteration = 1
        self.rho = 0.5  # < 1 to avoid unlimited accumulation of trail
        self.q = 0.3
        self.alpha = 0.02
        self.beta = 0.02

    """
    · if every ant has completed a tour, update_intensity on edge (i, j)
    · delta_quantity of the kth ant = q -constant- / L -tour length of the kth ant-
    · tours contains a list with every tour
    """
    def update_intensity(self, tours):
        # empty delta_matrix at the beginning of every cycle
        self.graph.delta_matrix.fill(0)

        for tour in tours:
            for connection in tour:
                p1 = self.graph.points_dict[connection[0]]
                p2 = self.graph.points_dict[connection[1]]

                delta_q = self.q / len(tour)

                self.graph.delta_matrix[p1, p2] += delta_q

        self.graph.trail_matrix = self.rho * self.graph.trail_matrix + self.graph.delta_matrix

    """
    "if on edge (i, j) there has been a lot of traffic the it is highly desirable"
    transition_probability calculates probs from point i to point j
    """
   # transition_probability from point i to j 
    def transition_probability(self):
        points_list = self.graph.point_set
        
        for ant in self.ants:
            allowed = points_list - ant.visited_points
            allowed_sum = 0




        
                
