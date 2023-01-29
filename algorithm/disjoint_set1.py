#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""
disjoint set with rank and path compression
improve time complexity to O(logn)
"""


class DisjointSet:
    def __init__(self, g=None):
        self.parent = {}
        self.rank = 0
        self.g = g  # graph
        if g:
            self.parent = {i: i for i in g.keys()}  # set each vertex as a set
            # set rank of each vertex equal to 0
            self.rank = dict.fromkeys(g.keys(), 0)

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
        # union all vertices with all their neighbors respectively
        for k in self.g.keys():
            for j in self.g[k]:
                self.union(k, j)
        vertices = list(self.g.keys())
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
        'f': ['d', 'e'],
        'g': []
    }
    my_djs1 = DisjointSet(graph1)
    print(my_djs1.is_cycle())
