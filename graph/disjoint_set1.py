#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""
disjoint set with rank and path compression
improve time complexity to O(logn)
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
        self.rank = 0
        self.g = g  # graph
        if g:
            # set each vertex as a set
            self.parent = {i: i for i in g.vertices}
            # set rank of each vertex equal to 0
            self.rank = dict.fromkeys(g.vertices, 0)

    def find(self, k):
        if self.parent[k] == k:
            return k
        else:  # path compression
            res = self.find(self.parent[k])  # get root
            self.parent[k] = res  # point k's parent to root
            return res

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        else:
            # always points the lower rank set to higher rank set
            if self.rank[x_root] > self.rank[y_root]:
                self.parent[y_root] = x_root
            elif self.rank[x_root] < self.rank[y_root]:
                self.parent[x_root] = y_root
            else:  # ranks of both set are the same
                # so it doesn't matter to point which set to another set
                # we need to rise the rank of parent
                self.parent[x_root] = y_root
                self.rank[y_root] += 1

    def is_cycle(self):
        for u, v in self.g.edges:
            u_root = self.find(u)
            v_root = self.find(v)
            if u_root == v_root:
                return True
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
