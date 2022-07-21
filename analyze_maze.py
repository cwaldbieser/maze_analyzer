#! /usr/bin/env python

from __future__ import print_function

import numpy as np
from scipy.sparse.csgraph import dijkstra


def main():
    """
    Analyze the maze.
    """
    connections = {
        1: [20, 26, 41, 21],
        2: [29, 22, 12],
        3: [33, 9, 18],
        4: [44, 29, 15, 11, 16, 24, 43],
        5: [43, 22, 30, 20],
        6: [40],
        7: [33, 36, 16],
        8: [31, 6, 29, 12],
        9: [3, 18],
        10: [34, 41, 14],
        11: [40, 24],
        12: [2, 21, 8, 39],
        13: [27, 18, 25],
        14: [10, 43, 24],
        15: [30, 37, 3],
        16: [36, 7],
        17: [6, 45, 33],
        18: [13, 3],
        19: [31, 11],
        20: [5, 27, 1],
        21: [44, 24, 31],
        22: [43, 38],
        23: [28, 8, 45, 19],
        24: [],
        25: [34, 13, 35],
        26: [30, 36, 38, 1],
        27: [13, 9],
        28: [23, 43, 45, 32],
        29: [8, 40, 35, 2, 17],
        30: [42, 34, 5, 15],
        31: [44, 19, 21],
        32: [11, 6, 28, 16],
        33: [3, 35, 7],
        34: [10, 25],
        35: [33],
        36: [7, 16],
        37: [15, 10, 42, 20],
        38: [40, 22, 43],
        39: [11, 4, 12],
        40: [11, 6, 38],
        41: [1, 10, 38, 35],
        42: [22, 30, 4, 25, 37],
        43: [22, 38],
        44: [21, 18],
        45: [28, 17, 36, 19, 23],
    }
    graph = []
    for i in range(1, 46):
        edges = set(connections[i])
        row = []
        for j in range(1, 46):
            if j in edges:
                row.append(1)
            else:
                row.append(0)
        graph.append(row)
    graph = np.array(graph)
    dist_matrix, predecesors_fwd = dijkstra(
        graph, indices=0, unweighted=True, return_predecessors=True
    )
    print(dist_matrix)
    print("")
    dist_matrix, predecesors_bwd = dijkstra(
        graph, indices=44, unweighted=True, return_predecessors=True
    )
    print(dist_matrix)
    print("")
    end_idx = 44
    order = ["45"]
    while end_idx != 0:
        end_idx = predecesors_fwd[end_idx]
        order.append("{0}".format(end_idx + 1))
    order = list(reversed(order))
    print("Order: {0}".format("=>".join(order)))
    end_idx = 0
    order = ["1"]
    while end_idx != 44:
        end_idx = predecesors_bwd[end_idx]
        order.append("{0}".format(end_idx + 1))
    order = list(reversed(order))
    print("Order: {0}".format("=>".join(order)))


if __name__ == "__main__":
    main()
