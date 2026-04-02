"""
Algorithm implementation
"""

import numpy as np
from graph import Graph
from ant import Ant
from calculate import Calculate

"""
1. Graph
"""
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

graph.ants = ants
# initialize trail matrix 
graph.initialize_trail()
graph.initialize_dist(dist_list)

# delta matrix already initialize with 0s

# number of cycles
max_cycles = 50

"""
2. Main loop
"""
for cycle in range(max_cycles):

    # clean previous tour and previous visited_points
    for ant in graph.ants:
        ant.tour = []
        ant.visited_points = set()

    # initialize ants
    graph.initialize_ants()

    # place starting point in visited for every ant
    for ant in graph.ants:
        ant.visited_points.add(ant.starting_point)

    # choose next_point 
    for iter in range(graph.n_points - 1):
        calc.transition_probability()

    # back to starting point
    for ant in graph.ants:
        current_point = ant.tour[-1][1]
        ant.tour.append((current_point, ant.starting_point))

    # update trail
    tours = []
    for ant in graph.ants:
        tours.append(ant.tour)
    calc.update_intensity(tours)

print(ant1.tour)
print(ant2.tour)
print(ant3.tour)


