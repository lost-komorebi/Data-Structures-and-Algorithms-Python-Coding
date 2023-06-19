#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   warshall_transitive_closure.py
@Time    :   2023/06/19 22:13:53
@Author  :   komorebi 
'''
"""
Given a directed graph, find out if a vertex j is reachable from another vertex i for all vertex pairs (i, j) in the given graph.
time complexity: O(n^3)
"""




import pandas as pd
class Graph:
    def __init__(self, n) -> None:
        self.n = n
        self.edges = [[0]*n for i in range(n)]
        self.vertices = {}
        self.cn = 0  # a counter to record number of vertices in the graph

    def add_edge(self, u, v):
        if self.vertices.get(u) is None:
            self.vertices[u] = self.cn
            self.cn += 1
        if self.vertices.get(v) is None:
            self.vertices[v] = self.cn
            self.cn += 1
        self.edges[self.vertices[u]][self.vertices[v]] = 1

    def print_graph(self):
        vertices = list(self.vertices.keys())
        df = pd.DataFrame(data=self.edges, columns=vertices, index=vertices)
        print(df)

    def warshalls_algorithm(self):
        for k in range(self.n):
            print(f'Round {k}')
            self.print_graph()
            for i in range(self.n):
                for j in range(self.n):
                    # if self.edges[i][k] == 1 and self.edges[k][j] == 1, then self.edges[i][k] and self.edges[k][j] == 1
                    self.edges[i][j] = self.edges[i][j] or (
                        self.edges[i][k] and self.edges[k][j])


if __name__ == '__main__':

    g = Graph(4)
    g.add_edge('A', 'B')
    g.add_edge('D', 'C')
    g.add_edge('B', 'D')
    g.add_edge('D', 'A')

    print(g.warshalls_algorithm())
