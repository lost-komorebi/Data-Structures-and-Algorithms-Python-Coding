#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   knight_tour.py
@Time    :   2023/03/28 22:33:20
@Author  :   komorebi 
'''
"""
The object of the puzzle is to find a sequence of moves that allow the knight to visit every square on the board exactly once
solution: (depth first search)
"""




from graph import Graph, Vertex
def build_graph(board_size):
    knight_graph = Graph()
    # for each point on the chess, we need to find reachable points for it
    for row in range(board_size):
        for col in range(board_size):
            start = get_node_name(row, col, board_size)
            reachable_points = get_reachable_points(row, col, board_size)
            for point in reachable_points:
                knight_graph.add_edge(start, point)
    return knight_graph


def get_reachable_points(row, col, board_size):
    """ according to knight movement rule, we calculate all points that the knight can reach """
    points = []
    rules = [(-2, 1), (-2, -1), (-1, 2), (-1, -2),  # knight's movement is a shape of 'L'
             (1, 2), (1, -2), (2, 1), (2, -1)]
    for i in rules:
        new_row = row + i[0]
        new_col = col + i[1]
        if check_move_legal(new_row, new_col, board_size):
            new_point = get_node_name(new_row, new_col, board_size)
            points.append(new_point)
    return points


def get_node_name(row, col, board_size):
    """ convert coordinate to node number """
    return row * board_size + col


def check_move_legal(row, col, board_size):
    """ check if the move of the knight is legal """
    if 0 <= row < board_size and 0 <= col < board_size:  # row and col must both between the range of the board_size
        return True
    else:
        return False


def knight_tour(n, start: Vertex, depth, path):
    """
    n: the length of path, it means how many points the knight has already passed, we start from 0
    start: start vertex
    depth: the depth of this graph, because we start from 0, so the number eqaul to number of vertices in this graph - 1
    path: store the path of knight's movement
    """

    path.append(start)

    if n < depth:
        neighbors = list(start.get_connections())
        i = 0
        done = False
        # we will keep going until we visited all neighbors of current vertex or we have reached the end
        while i < len(neighbors) and not done:
            # this neighbor haven't been visited, so we try to visit this neighbor
            if neighbors[i] not in path:
                done = knight_tour(n + 1, neighbors[i], depth, path)
            i += 1
        # dead end, because we visited all neighbors of current vertex, but we still haven't reached the end
        if not done:
            path.pop()  # backtrack
    else:
        done = True
    return done


if __name__ == '__main__':
    g = build_graph(8)
    number = len(g.get_vertices()) - 1
    start = g.get_vertex(0)
    path = []
    knight_tour(0, start, number, path)
    print([x.get_name() for x in path], len(path))
