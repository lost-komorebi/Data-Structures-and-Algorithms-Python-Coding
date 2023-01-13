#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""
using adjacency matrix to represent directed and undirected, weighted and unweighted graph
"""


class Vertex:
    def __init__(self, name):
        self.name = name


class Graph:
    def __init__(self, direct=0, weight=0):
        self.graph = {}  # store vertex object
        self.edges = []  # store adjacency matrix
        self.direct = direct  # 0 undirected; 1 directed
        self.weight = weight  # 0 unweighted; 1 weighted

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.graph:
            self.graph[vertex.name] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * len(self.graph))

    def add_edge(self, vertex1, vertex2, weight=None):
        if vertex1 in self.graph and vertex2 in self.graph:
            index1 = list(self.graph.keys()).index(vertex1)
            index2 = list(self.graph.keys()).index(vertex2)
            if self.weight == 0:
                self.edges[index1][index2] = 1
            else:
                self.edges[index1][index2] = weight
            if self.direct == 0:  # vertex1 and vertex2 point to each other
                if self.weight == 0:
                    self.edges[index2][index1] = 1
                else:
                    self.edges[index2][index1] = weight

    def print_graph(self):
        print('  ' + ' '.join(self.graph.keys()))
        for i in self.graph.keys():
            print(i + ' ', end='')
            index = list(self.graph.keys()).index(i)
            for j in range(len(self.graph)):
                print(self.edges[index][j], end=' ')
            print(' ')


if __name__ == '__main__':
    # undirected unweighted
    uu_graph = Graph()
    for i in range(ord('a'), ord('h') + 1):
        uu_graph.add_vertex(Vertex(chr(i)))
    edges = ['ac', 'bc', 'bd', 'ce', 'df', 'eh', 'ef', 'fg']
    for i in edges:
        uu_graph.add_edge(i[0], i[-1])
    print('undirected unweighted graph')
    uu_graph.print_graph()

    # undirected weighted
    uw_graph = Graph(weight=1)
    for i in range(ord('a'), ord('h') + 1):
        uw_graph.add_vertex(Vertex(chr(i)))
    edges = ['ac1', 'bc2', 'bd3', 'ce4', 'df5', 'eh6', 'ef7', 'fg8']
    for i in edges:
        uw_graph.add_edge(i[0], i[1], i[-1])
    print('undirected weighted graph')
    uw_graph.print_graph()

    # directed unweighted
    du_graph = Graph(direct=1)
    for i in range(ord('a'), ord('h') + 1):
        du_graph.add_vertex(Vertex(chr(i)))
    edges = ['ac', 'bc', 'bd', 'ce', 'df', 'eh', 'ef', 'fg']
    for i in edges:
        du_graph.add_edge(i[0], i[-1])
    print('directed unweighted graph')
    du_graph.print_graph()

    # directed weighted
    dw_graph = Graph(direct=1, weight=1)
    for i in range(ord('a'), ord('h') + 1):
        dw_graph.add_vertex(Vertex(chr(i)))
    edges = ['ac1', 'bc2', 'bd3', 'ce4', 'df5', 'eh6', 'ef7', 'fg8']
    for i in edges:
        dw_graph.add_edge(i[0], i[1], i[-1])
    print('directed weighted graph')
    dw_graph.print_graph()
