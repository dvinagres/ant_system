"""
Evaluation function
"""

def calculate_distance(graph, tour_list):
    distance = 0

    for edge in tour_list:
        p1 = graph.points_dict[edge[0]]
        p2 = graph.points_dict[edge[1]]

        distance += graph.dist_matrix[p1, p2]

    return distance

