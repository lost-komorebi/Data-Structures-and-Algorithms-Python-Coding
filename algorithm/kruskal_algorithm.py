#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""
perform kruskal algorithm and disjoint set to find minimum spanning tree
step 1: sort all edges order by weights
step 2: add increasing cost edges at each step
step 3: avoid any cycle at each step
"""


class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, name):
        self.vertices.append(name)

    def add_edge(self, u, v, w):
        self.edges.append([u, v, w])


class Kruskal:
    def __init__(self, g: Graph):
        self.g = g
        self.parent = {i: i for i in g.vertices}
        self.rank = {i: 0 for i in g.vertices}

    def find(self, k):
        if self.parent[k] == k:
            return k
        else:
            res = self.find(self.parent[k])
            self.parent[k] = res
            return res

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        else:
            if self.rank[x_root] > self.rank[y_root]:
                self.parent[y_root] = x_root
            elif self.rank[x_root] < self.rank[y_root]:
                self.parent[x_root] = y_root
            else:
                self.parent[x_root] = y_root
                self.rank[y_root] += 1

    def kruskal(self):
        # sort all edges order by weight
        self.g.edges = sorted(self.g.edges, key=lambda x: x[2])
        mst_value = 0  # minimum spanning tree
        visited = set()
        paths = []
        for u, v, w in self.g.edges:
            u_root = self.find(u)
            v_root = self.find(v)
            if u_root != v_root:  # avoid any cycle
                mst_value += w  # add increasing cost
                paths.append([u, v, mst_value])
                visited.add(u)
                visited.add(v)
                self.union(u_root, v_root)
        if len(visited) != len(self.g.vertices):
            print('cannot find minimum spanning tree')
        else:
            print('minimum spanning tree:')
            for i in paths:
                print(i)


if __name__ == '__main__':
    g1 = Graph()
    for i in range(97, 97 + 5):
        g1.add_vertex(chr(i))
    edges = ['ab5', 'ae15', 'ac13', 'bc10', 'bd8', 'ce20', 'cd6']
    for edge in edges:
        g1.add_edge(edge[0], edge[1], int(edge[2:]))
    k = Kruskal(g1)
    k.kruskal()

    g2 = Graph()
    for i in range(97, 97 + 5):
        g2.add_vertex(chr(i))
    edges = ['ab5', 'ac13', 'bc10', 'bd8', 'cd6']
    for edge in edges:
        g2.add_edge(edge[0], edge[1], int(edge[2:]))
    k = Kruskal(g2)
    k.kruskal()
