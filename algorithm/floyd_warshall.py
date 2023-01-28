#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""
floyd warshall algorithm needs iterate N times, N is number of vertices
The Floyd Warshall Algorithm is for solving all pairs of shortest-path problems.
The problem is to find the shortest distances between every pair of vertices
in a given edge-weighted directed Graph.
"""


class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, name):
        self.vertices.append(name)
        # generate edges 2d array, set default weight as infinity
        for row in self.edges:
            row.append(float('inf'))
        self.edges.append([float('inf')] * len(self.vertices))
        # start and end is the same vertex, set weight as 0
        for i in range(len(self.vertices)):
            self.edges[i][i] = 0

    def add_edge(self, start, end, weight):
        #  update weight of edges
        idx_start = self.vertices.index(start)
        idx_end = self.vertices.index(end)
        self.edges[idx_start][idx_end] = weight

    def print_graph(self):
        print('  ' + ' '.join(self.vertices))
        for i in range(len(self.vertices)):
            print(self.vertices[i] + ' ', end='')
            for j in range(len(self.vertices)):
                print(self.edges[i][j], end=' ')
            print(' ')


def floyd_warshall(graph):
    n = len(graph)

    for _ in range(n):
        # pick all vertices as source one by one
        for i in range(n):
            # Pick all vertices as destination for the
            # above picked source
            for j in range(n):
                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                graph[i][j] = min(graph[i][j], graph[i][_] + graph[_][j])


if __name__ == '__main__':
    my_graph = Graph()
    my_graph.add_vertex('a')
    my_graph.add_vertex('b')
    my_graph.add_vertex('c')
    my_graph.add_vertex('d')
    my_graph.add_edge('a', 'b', 8)
    my_graph.add_edge('a', 'd', 1)
    my_graph.add_edge('b', 'c', 1)
    my_graph.add_edge('c', 'a', 4)
    my_graph.add_edge('d', 'b', 2)
    my_graph.add_edge('d', 'c', 9)
    my_graph.print_graph()
    floyd_warshall(my_graph.edges)
    my_graph.print_graph()
