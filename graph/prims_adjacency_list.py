#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   prims_adjacency_list.py
@Time    :   2023/06/18 14:59:00
@Author  :   komorebi 
'''

"""
prim's alogrithm by using adjacency list and heapq
1. choose an arbitrary vertex, add it to the mst and add it's all edges to a heap
2. while the heap is not empty:
    pop the edge with smallest weight and add the edge's another endpoint to mst if the edge's another endpoint is not in the mst
    
"""




import heapq
from collections import defaultdict
class Graph:
    def __init__(self) -> None:
        self.vertices = defaultdict(list)

    def add_edge(self, u, v, w):
        if not self.vertices.get(v):
            self.vertices[v] = []
        self.vertices[u].append((v, w))
        self.vertices[v].append((u, w))

    def prims(self):
        vertices = list(self.vertices.keys())
        source = vertices[0]  # choose first vertex as source
        mst = set(source)
        h = []
        for v, w in self.vertices[source]:  # push source's all edges in the heap
            heapq.heappush(h, (w, source, v))
        while h:
            w, u, v = heapq.heappop(h)  # extract minimum weight edge
            if v not in mst:  # add another endpoint to the mst
                print(u, v, w)
                mst.add(v)
                # find v's neighbors and push into the heap
                for n, w in self.vertices[v]:
                    if n not in mst:
                        heapq.heappush(h, (w, v, n))


if __name__ == '__main__':

    g = Graph()
    g.add_edge('E', 'C', 20)
    g.add_edge('A', 'B', 5)
    g.add_edge('A', 'C', 13)
    g.add_edge('C', 'D', 6)
    g.add_edge('B', 'D', 8)
    g.add_edge('A', 'E', 15)
    g.add_edge('E', 'D', 33)
    g.add_edge('A', 'D', 44)
    g.add_edge('E', 'B', 66)
    g.add_edge('C', 'B', 10)
    g.prims()
