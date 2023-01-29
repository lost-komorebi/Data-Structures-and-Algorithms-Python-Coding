#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""
two or more set without any element in common called disjoint sets
"""


class DisjointSet:
    def __init__(self, g=None):
        self.parent = {}
        if g:  # init parent, each vertex as them parents
            for vertex in g.keys():
                self.parent[vertex] = vertex

    def find(self, k):
        """ find the representative to represent this set"""
        if k == self.parent[k]:  # if k equal to parent[k], it means k is the representative of this set
            return k
        # otherwise we will call this function recursively to find the
        # representative
        return self.find(self.parent[k])

    def union(self, x, y):
        """ put x and y in a set """
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:  # x and y already in same set
            return
        self.parent[x_root] = y_root  # points the root of x to the root of y

    def is_cycle(self, graph):
        # union all vertices with their neighbors respectively
        for k in graph.keys():
            for j in graph[k]:
                self.union(k, j)
        vertices = list(graph.keys())
        # iterate all vertices to check if they are in same set
        # then it is a cycle graph
        for i in range(len(vertices) - 1):
            if self.find(vertices[i]) != self.find(vertices[i + 1]):
                return False
        return True


if __name__ == '__main__':
    graph1 = {
        'a': ['b', 'c'],
        'b': ['a', 'd'],
        'c': ['a', 'd', 'e'],
        'd': ['c', 'b', 'f'],
        'e': ['c', 'f'],
        'f': ['d', 'e', 'g'],
        'g': ['b', 'f']
    }
    my_djs1 = DisjointSet(graph1)
    print(my_djs1.is_cycle(graph1))

    graph2 = {
        'a': ['b', 'c'],
        'b': ['a', 'd'],
        'c': ['a', 'd', 'e'],
        'd': ['c', 'b', 'f'],
        'e': ['c', 'f'],
        'f': ['d', 'e'],
        'g': []
    }
    my_djs2 = DisjointSet(graph2)
    print(my_djs2.is_cycle(graph2))
