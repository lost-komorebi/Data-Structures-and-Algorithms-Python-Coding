#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.distance_map = {}  # set distance of all nodes as infinity
        self.path_map = {}  # store vertex:prev_vertex pair

    def add_node(self, name):
        self.nodes.append(name)
        self.distance_map[name] = float('inf')
        self.path_map[name] = None

    def add_edge(self, start, end, weight):
        self.edges.append([start, end, weight])

    def _bellman(self, start_vertex):
        # set distance of start_vertex as 0
        self.distance_map[start_vertex] = 0
        for i in range(len(self.nodes) - 1):  # loop len(self.nodes) - 1 times
            for start, end, weight in self.edges:
                if self.distance_map[start] + weight < self.distance_map[end]:
                    self.distance_map[end] = self.distance_map[start] + weight
                    self.path_map[end] = start
        del self.path_map[start_vertex]  # delete path from start_vertex to itself

        # loop one more time to check if this graph a negative cycle
        for start, end, weight in self.edges:
            if self.distance_map[start] + weight < self.distance_map[end]:
                print('this graph contains negative cycle')
                return False
        return True

    def bellman(self, start_vertex):
        
        if self._bellman(start_vertex):
            # generate readable path
            paths = {}
            for i in self.path_map:
                path = [i]
                while path[-1] != start_vertex:
                    path.append(self.path_map[path[-1]])
                path.reverse()
                path = ' -> '.join(path)
                paths[i] = path
            for i in self.distance_map:
                if i != start_vertex:
                    print(f'the shortest distance from {start_vertex} to {i} is {self.distance_map[i]}, {paths[i]}')


if __name__ == '__main__':
    # graph with no negative edge
    my_graph1 = Graph()
    my_graph1.add_node('a')
    my_graph1.add_node('b')
    my_graph1.add_node('c')
    my_graph1.add_node('e')
    my_graph1.add_node('d')
    my_graph1.add_edge('a', 'c', 6)
    my_graph1.add_edge('a', 'd', 6)
    my_graph1.add_edge('b', 'a', 3)
    my_graph1.add_edge('c', 'd', 1)
    my_graph1.add_edge('d', 'c', 2)
    my_graph1.add_edge('d', 'b', 1)
    my_graph1.add_edge('e', 'b', 4)
    my_graph1.add_edge('e', 'd', 2)
    my_graph1.bellman('e')
    print(' ')

    # graph with no negative edge
    my_graph2 = Graph()
    my_graph2.add_node('a')
    my_graph2.add_node('b')
    my_graph2.add_node('c')
    my_graph2.add_node('e')
    my_graph2.add_node('d')
    my_graph2.add_edge('a', 'c', 6)
    my_graph2.add_edge('a', 'd', -6)
    my_graph2.add_edge('b', 'a', 3)
    my_graph2.add_edge('c', 'd', 1)
    my_graph2.add_edge('d', 'c', 2)
    my_graph2.add_edge('d', 'b', 1)
    my_graph2.add_edge('e', 'b', 4)
    my_graph2.add_edge('e', 'd', 2)
    my_graph2.bellman('e')
