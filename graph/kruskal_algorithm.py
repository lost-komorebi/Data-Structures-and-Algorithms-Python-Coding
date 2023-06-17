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
        # recode the number of vertex of this set
        self.rank = {i: 1 for i in g.vertices}

    def find(self, k):
        if self.parent[k] == k:
            return k
        else:  # path compression
            res = self.find(self.parent[k])  # get root
            # point k's parent to root, to reduce find time for next finding
            self.parent[k] = res
            return res

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        else:  # always choose the heavier set as the parent of lighter set
            if self.rank[x_root] >= self.rank[y_root]:
                self.parent[y_root] = x_root
                self.rank[x_root] += self.rank[y_root]
            else:
                self.parent[x_root] = y_root
                self.rank[y_root] += self.rank[x_root]

    def kruskal(self):
        # sort all edges order by weight
        sorted_edges = sorted(self.g.edges, key=lambda x: x[2])
        mst_value = 0  # minimum spanning tree
        visited = set()
        paths = []
        # counter i for loop throught all edges, counter e for keeping track of number of edges
        # for a graph with n vertices, we just need n - 1 edges to connect all vertices
        i, e = 0, 0
        total_vertices = len(self.g.vertices)
        total_edges = len(self.g.edges)
        while e < total_vertices - 1 and i < total_edges:
            u, v, w = sorted_edges[i]
            i += 1
            u_root = self.find(u)
            v_root = self.find(v)
            if u_root != v_root:  # avoid any cycle
                e += 1
                mst_value += w  # add increasing cost
                paths.append([u, v, mst_value])
                visited.add(u)
                visited.add(v)
                self.union(u_root, v_root)
        # check if all vertices in a set
        # if all vertices in a set, then it's a mst
        # otherwise it's not a mst
        parent = self.find(list(visited)[0])
        for i in visited:
            if self.find(i) != parent:
                print('cannot find minimum spanning tree for current graph')
                return
        else:
            print('minimum spanning tree:')
            for i in paths:
                print(i)


if __name__ == '__main__':
    # connected graph
    g1 = Graph()
    g1.add_vertex('A')
    g1.add_vertex('B')
    g1.add_vertex('C')
    g1.add_vertex('D')
    g1.add_vertex('E')
    g1.add_edge('A', 'E', 15)
    g1.add_edge('E', 'C', 20)
    g1.add_edge('A', 'C', 13)
    g1.add_edge('B', 'D', 8)
    g1.add_edge('A', 'B', 5)
    g1.add_edge('C', 'D', 6)
    g1.add_edge('C', 'B', 10)
    g1.add_edge('E', 'D', 33)
    g1.add_edge('A', 'D', 44)
    g1.add_edge('E', 'B', 66)
    k1 = Kruskal(g1)
    k1.kruskal()

    # disconnected graph
    g2 = Graph()
    g2.add_vertex('A')
    g2.add_vertex('B')
    g2.add_vertex('C')
    g2.add_vertex('D')
    g2.add_vertex('E')
    g2.add_edge('A', 'E', 15)
    g2.add_edge('E', 'C', 20)
    g2.add_edge('A', 'C', 13)
    g2.add_edge('B', 'D', 8)
    k2 = Kruskal(g2)
    k2.kruskal()
