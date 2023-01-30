#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""
perform prims algorithm to find minimum spanning tree for a weighted undirected graph
1. Take any vertex as a source set its weight to 0 and all other vertices’ weight to infinity
2. For every adjacent vertices if the current weight is more than current edge then we set it
to current edge
3. Then we mark current vertex as visited
4. Repeat these steps for all vertices in increasing order of weight
"""

from floyd_warshall import Graph


class MyGraph(Graph):
    def __init__(self):
        super(MyGraph, self).__init__()

    def add_edge(self, start, end, weight):
        #  update weight of edges
        idx_start = self.vertices.index(start)
        idx_end = self.vertices.index(end)
        self.edges[idx_start][idx_end] = weight
        # undirected graph
        self.edges[idx_end][idx_start] = weight


def prims(graph: Graph):
    src = graph.vertices[0]  # start from src
    visited = set(src)  # visited vertices
    n = len(graph.vertices)
    print(graph.print_graph())
    for i in range(n - 1):  # start from src, initially i = 0
        # define a variable to store the smallest weight from current vertex's
        # neighbors
        min_weight = float('inf')
        for j in range(n):
            # graph.vertices[j] not in visited means to skip visited vertices
            # i != j means to skip check weight from vertex to itself
            # graph.edges[i][j] != float('inf') means neighbors of
            # graph.vertices[i]
            if graph.vertices[j] not in visited and i != j and graph.edges[i][j] != float(
                    'inf'):
                # find vertex which has the smallest weight from current
                # vertex's neighbors
                if min_weight > graph.edges[i][j]:
                    min_weight = graph.edges[i][j]
                    s = j  # define a variable to store current j, because j is increasing
        # all neighbors of graph.vertices[i] have been checked, mark
        # graph.vertices[i] as visited
        visited.add(graph.vertices[i])
        print(graph.vertices[i], graph.vertices[s], min_weight)


if __name__ == '__main__':
    my_graph = MyGraph()
    my_graph.add_vertex('a')
    my_graph.add_vertex('b')
    my_graph.add_vertex('c')
    my_graph.add_vertex('d')
    my_graph.add_vertex('e')
    my_graph.add_edge('a', 'b', 10)
    my_graph.add_edge('a', 'c', 20)
    my_graph.add_edge('b', 'c', 30)
    my_graph.add_edge('b', 'd', 5)
    my_graph.add_edge('c', 'd', 15)
    my_graph.add_edge('c', 'e', 6)
    my_graph.add_edge('d', 'e', 8)
    prims(my_graph)
