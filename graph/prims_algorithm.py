#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""
perform prims algorithm to find minimum spanning tree for a weighted undirected graph by using matrix represtation
time complexity: O(V^2)

1. divide the graph to two parts: one is all nodes in mst, another is all nodes not in mst
2. create a set to store all vertices that are already in mst
3. define a distances dict to store the distance to the mst from all nodes that are not in the mst 
in the distances dict set all node's value to infinity and choose an arbitrary node set the distance to 0, this node will be the first node in mst
4. while mst doesn't include all vertices:
    a. pick a vertex 'v' that is not in the mst but has a minimum distance to the mst
    b. add the vertex 'v' into the mst
    c. update the distances value of all neighbors of u, if the weight of edge from u to its neighbor
    less than the distances value, update the distance value as the weight of edge from u to its neighbor
"""
import pandas as pd


class Graph:
    def __init__(self, n):
        self.n = n  # the total number of vertices
        self.vertices = {}
        # set default distance as infinity for all edges
        self.edges = [[float('inf')] * n for i in range(n)]

    def add_edge(self, start, end, weight):
        if start not in self.vertices:
            self.vertices[start] = start
        if end not in self.vertices:
            self.vertices[end] = end
        #  update weight of edges
        idx_start = list(self.vertices.keys()).index(start)
        idx_end = list(self.vertices.keys()).index(end)
        self.edges[idx_start][idx_end] = weight
        # undirected graph
        self.edges[idx_end][idx_start] = weight

    def print_graph(self):
        df = pd.DataFrame(self.edges, columns=list(
            self.vertices.keys()), index=list(self.vertices.keys()))
        print(df)

    def fin_min(self, distances, mst):
        """
        find the vertex that is not in mst but has a minimum distance to the mst
        """
        min_distance = float('inf')
        for i in distances:
            if min_distance > distances[i] and i not in mst:
                min_distance = distances[i]
                min_vertex = i
        return min_vertex

    def print_solution(self, parent):
        for k, v in parent.items():
            if v != -1:
                print(f'{k} {v[0]} {v[1]}')

    def prims(self):
        vertices = list(self.vertices.keys())
        # store the distance to the mst from all nodes that are not in the mst
        distances = {v: float('inf') for v in vertices}
        source = vertices[0]  # start from first vertex
        distances[source] = 0
        mst = set()  # store vertices that are already in the mst
        parent = {source: -1}
        for i in range(self.n):
            v = self.fin_min(distances, mst)
            v_index = vertices.index(v)
            mst.add(v)
            for j in range(self.n):
                # vertices[j] is neighbor of v, reachable
                # vertices[j] not in mst
                # the weight of edge from v to its neighbor less than the distances value
                if self.edges[v_index][j] != float('inf') and \
                        vertices[j] not in mst and \
                        distances[vertices[j]] > self.edges[v_index][j]:
                    distances[vertices[j]] = self.edges[v_index][j]
                    parent[vertices[j]] = (v, self.edges[v_index][j])
        self.print_solution(parent)


if __name__ == '__main__':

    g = Graph(5)
    g.add_edge('A', 'B', 5)
    g.add_edge('A', 'C', 13)
    g.add_edge('C', 'D', 6)
    g.add_edge('E', 'C', 20)
    g.add_edge('B', 'D', 8)
    g.add_edge('A', 'E', 15)
    g.add_edge('E', 'D', 33)
    g.add_edge('A', 'D', 44)
    g.add_edge('E', 'B', 66)
    g.add_edge('C', 'B', 10)

    g.print_graph()
    g.prims()
