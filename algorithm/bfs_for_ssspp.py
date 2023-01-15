#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

""" breadth first traversal for single source shortest path problem in unweighted graph"""

from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, v1, v2):
        self.graph[v1].append(v2)

    def bfs(self, start):
        """ breadth first search """
        q = deque(start)
        visited = []  # mark all vertices as unvisited
        while q:
            p = q.popleft()
            if p not in visited:
                visited.append(p)
            for i in self.graph[p]:  # loop all neighbors of vertex p
                if i not in visited:  # avoid visiting vertex a second time
                    q.append(i)
        print(visited)

    def shortest_path(self, start, end):
        """ find the shortest path from a to b"""
        # init queue to store all paths from start to all vertices
        q = deque([start])
        while q:
            path = q.popleft()
            vertex = path[-1]  # get last vertex from path
            # compare if last vertex of path equal to our end, if equal to, it
            # means we have arrived the end
            if vertex == end:
                return path
            # otherwise we will continue to all neighbors of current vertex
            for neighbor in self.graph.get(vertex, []):
                new_path = list(path)  # copy path from start to current vertex
                new_path.append(neighbor)  # add neighbor to old path
                # new_path is the shorted path from start to neighbors
                q.append(new_path)


if __name__ == '__main__':
    my_graph = Graph()
    """ example from ../graph/graph_matrix.png """
    edges = ['ac', 'bc', 'bd', 'ce', 'df', 'eh', 'ef', 'fg']
    for i in edges:
        my_graph.add_edge(i[0], i[-1])
    print(my_graph.graph)
    print(my_graph.bfs('a'))
    print(my_graph.shortest_path('a', 'f'))
