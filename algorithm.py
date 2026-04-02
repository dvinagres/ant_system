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

"""
· initialize ants starting point
· initialize trail matrix 
· delta matrix already initialize with 0s
"""
graph.ants = ants
graph.initialize_ants()
graph.initialize_trail()




