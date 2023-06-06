#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   graph_dfs_without_using_stack.py
@Time    :   2023/06/05 21:40:53
@Author  :   komorebi 
'''
"""
1. Create a recursive function that takes a vertex and parent dictionary, this function will visit as deep as possible.
If the neighbor of current vertex is not visited, add the neighbor into parent dictionary and call the recursive function with the neighbor.
2. Loop through all vertices in the graph, check if the vertex is unvisited, then call the recursive function  with current vertex.

This algorithm can handle with disconnected graphs
time complexity: O(V+E)
"""




from collections import defaultdict
class Graph:
    def __init__(self) -> None:
        self.vertices = defaultdict(list)

    def add_edge(self, s, t):
        if t not in self.vertices:  # add all vertices into the graph to avoid 'dictionary changed size during iteration' error
            self.vertices[t] = []
        self.vertices[s].append(t)

    def dfs(self):
        parent = {}  # record the from node of the node
        for v in self.vertices.keys():
            if v not in parent:
                parent[v] = None
                self.dfs_visit(v, parent)
        print(list(parent.keys()))

    def dfs_visit(self, v, parent):
        for n in self.vertices[v]:
            if n not in parent:  # n is not visited
                parent[n] = v
                # continue visiting a neighbor of vertex n as deep as possible
                self.dfs_visit(n, parent)


if __name__ == '__main__':

    directed = ['AB', 'BC', 'CE', 'ED', 'DB', 'EF']
    undirected = ['AB', 'BA', 'BC', 'CB', 'CE',
                  'EC', 'EF', 'FE', 'ED', 'DE', 'DB', 'BD']

    directed_graph = Graph()
    for i in directed:
        directed_graph.add_edge(i[0], i[1])

    undirected_graph = Graph()
    for i in undirected:
        undirected_graph.add_edge(i[0], i[1])

    directed_graph.dfs()
    undirected_graph.dfs()
