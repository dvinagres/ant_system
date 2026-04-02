"""
Algorithm implementation
"""

import numpy as np
from graph import Graph
from ant import Ant
from calculate import Calculate
from evaluate import calculate_distance

"""
1. Graph
"""
# complete graph
points = ["a", "b", "c", "d", "e", "f", "g", "h"]
edge_list = [("a", "b"), ("a", "c"), ("a", "d"), ("a", "e"), ("a", "f"), ("a", "g"), ("a", "h"),
             ("b", "c"), ("b", "d"), ("b", "e"), ("b", "f"), ("b", "g"), ("b", "h"),
             ("c", "d"), ("c", "e"), ("c", "f"), ("c", "g"), ("c", "h"),
             ("d", "e"), ("d", "f"), ("d", "g"), ("d", "h"),
             ("e", "f"), ("e", "g"), ("e", "h"),
             ("f", "g"), ("f", "h"),
             ("g", "h")]

graph = Graph(points, edge_list, 5)
ant1 = Ant(1, graph)
ant2 = Ant(2, graph)
ant3 = Ant(3, graph)
ant4 = Ant(4, graph)
ant5 = Ant(5, graph)
ants = [ant1, ant2, ant3, ant4, ant5]

calc = Calculate(graph, ants)

dist_list = [15, 22, 14, 30, 12, 25, 18, 
             19, 26, 35, 17, 21, 10,     
             11, 24, 31,  9, 16,         
             28, 13, 20, 33,             
             27, 29, 23,                 
             14, 32,                     
             21]

graph.ants = ants
# initialize trail matrix 
graph.initialize_trail()
graph.initialize_dist(dist_list)

# delta matrix already initialize with 0s

# number of cycles
max_cycles = 50

# store results
best_distance = float("inf")
best_tour = None

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

    # evaluation
    for ant in graph.ants:
        evaluation = calculate_distance(graph, ant.tour)
        if evaluation < best_distance:
            best_distance = evaluation
            best_tour = ant.tour

    # update trail
    tours = []
    for ant in graph.ants:
        tours.append(ant.tour)
    calc.update_intensity(tours)

"""
3. Results
"""
print(f"Shortest tour: {best_tour}")
print(f"Distance: {best_distance}")




