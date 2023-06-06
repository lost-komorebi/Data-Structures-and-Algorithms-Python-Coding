#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   graph_bfs_without_using_queue.py
@Time    :   2023/06/05 21:40:29
@Author  :   komorebi 
'''
"""
step 1: Choose a start vertex, define a frontier list to store all vertices for iteration(the initial value is the start vertex), 
a parent dictionary to store the predecessor(the initial key is the start vertex and set the value to None), 
a level dictionary to store the level of all vertices(the initial key is the start vertex and set the value to 1)
step 2: Loop through frontier list, define a next list. 
If the vertex is not existed in the parent dictionary, then add it to the parent dictionary, the level dictionary, and the next list.
step 3: Replace frontier with next and increase level by one.
step 4: Repeat step 1 and 2 until frontier is empty.
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

    def bfs(self, s):
        # record the level for the node, the level of start node is 0.
        level = {s: 0}
        parent = {s: None}  # record the from node of the node
        i = 1  # intial value for level
        frontier = [s]
        # record visited nodes, after looping throught all nodes, this is the bfs path
        visited = [s]
        while frontier:
            next = []
            for v in frontier:
                for n in self.vertices[v]:
                    if n not in parent:
                        parent[n] = v
                        level[n] = i
                        next.append(n)
                        visited.append(n)
            frontier = next
            i += 1
        # print(level)
        # print(parent)
        print(visited)


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

    directed_graph.bfs('A')
    undirected_graph.bfs('A')
