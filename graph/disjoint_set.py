#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""
two or more set without any element in common called disjoint sets
"""


class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, name):
        self.vertices.append(name)

    def add_edge(self, u, v):
        self.edges.append([u, v])


class DisjointSet:
    def __init__(self, g: Graph = None):
        self.parent = {}
        self.g = g
        if g:  # Initially create subsets containing only a single node which are the parent of itself
            for vertex in g.vertices:
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

    def is_cycle(self):
        # iterate all edges
        for u, v in self.g.edges:
            # if the two end nodes of the edge belongs to the same set then
            # they form a cycle
            u_root = self.find(u)
            v_root = self.find(v)
            if u_root == v_root:
                return True
            # perform union to merge the subsets together
            self.union(u_root, v_root)
        return False


if __name__ == '__main__':
    graph1 = Graph()
    graph1.add_vertex('a')
    graph1.add_vertex('b')
    graph1.add_vertex('c')
    graph1.add_vertex('d')
    graph1.add_edge('a', 'b')
    graph1.add_edge('b', 'c')
    graph1.add_edge('c', 'd')
    graph1.add_edge('d', 'a')

    my_djs1 = DisjointSet(graph1)
    print(my_djs1.is_cycle())

    print('>>>>>>')

    graph2 = Graph()
    graph2.add_vertex('a')
    graph2.add_vertex('b')
    graph2.add_vertex('c')
    graph2.add_vertex('d')
    graph2.add_edge('a', 'b')
    graph2.add_edge('b', 'c')
    graph2.add_edge('c', 'd')

    my_djs2 = DisjointSet(graph2)
    print(my_djs2.is_cycle())
