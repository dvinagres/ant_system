"""
Algorithm implementation
"""

import numpy as np
from graph import Graph
from ant import Ant
from calculate import Calculate

# 1. Graph
# complete graph
points = ["a", "b", "c", "d", "e"]
edge_list = [("a", "b"), ("a", "c"), ("a", "d"), ("a", "e"),
             ("b", "c"), ("b", "d"), ("b", "e"),
             ("c", "d"), ("c", "e"),
             ("d", "e")]

graph = Graph(points, edge_list, 3)
ant1 = Ant(1, graph)
ant2 = Ant(2, graph)
ant3 = Ant(3, graph)
ants = [ant1, ant2, ant3]
calc = Calculate(graph, ants)
dist_list = [1, 5, 3, 6, 3, 4, 5, 8, 9, 2]

"""
· initialize ants starting point
· initialize trail matrix 
· delta matrix already initialize with 0s
"""
graph.ants = ants
graph.initialize_ants()
graph.initialize_trail()
graph.initialize_dist(dist_list)

# 2. Place starting point in visited for every ant
for ant in graph.ants:
    ant.visited_points.add(ant.starting_point)

# 3. Choose next_point    
calc.transition_probability()




