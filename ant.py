"""
Ant implementation
"""
from graph import Graph

class Ant:

    def __init__(self, id):
        self.id = id
        self.visited_points = set()
        self.graph = Graph(0, [], 0)
        self.starting_point = self.graph.points_dict[0] # Default start

    # goal_completed confirms if the problem is solved
    def goal_completed(self, next_point):
        completed = False
        if len(self.visited_points) == self.graph.n_points and next_point == self.starting_point:
            completed = True
        return completed
    
    # if tour completed, leave_trail on edge (i, j)
    # tour contains a list with tuples
    def leave_trail(self, tour, completed):

