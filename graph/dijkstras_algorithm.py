#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
""" Dijkstra's Algorithm for shortest path problem in weighted graph """

import heapq  # use python built-in library to maintain heap data structure


class Edge:
    def __init__(self, weight, start_vertex, end_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex


class Node:
    def __init__(self, name):
        self.name = name
        self.prev = None  # from which node to current node the distance is shortest
        # assume the distance from any node to current node is infinity
        self.min_distance = float('inf')
        self.neighbors = []  # a variable to store all neighbors
        self.visited = False

    # let node be comparable, thus allowing us to use heap structure to store
    # nodes
    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance

    def add_edge(self, weight, end_vertex):
        edge = Edge(weight=weight, start_vertex=self, end_vertex=end_vertex)
        self.neighbors.append(edge)


class Dijkstras:
    def __init__(self):
        self.heap = []

    def _calculate(self, start_vertex: Node):
        """ calculate the path and distance from start_vertex to any other reachable node that in graph """
        start_vertex.min_distance = 0
        heapq.heappush(self.heap, start_vertex)  # add new node to heap
        while self.heap:
            cur_vertex = heapq.heappop(
                self.heap)  # get smallest node from heap
            if cur_vertex.visited:
                continue
            for edge in cur_vertex.neighbors:
                end = edge.end_vertex
                new_distance = cur_vertex.min_distance + edge.weight
                # we only update min_distance and prev when we find a shorter
                # path
                if new_distance < end.min_distance:
                    # min_distance is the shortest distance from start_vertex
                    # to cur_vertex
                    end.min_distance = new_distance
                    end.prev = cur_vertex
                    heapq.heappush(self.heap, end)
            # all neighbors of cur_vertex are calculated, set cur_vertex as
            # visited
            cur_vertex.visited = True

    def get_shorted_path(self, start, destination):
        self._calculate(start)
        print(
            f'the shortest distance from {start.name} to {destination.name} is {destination.min_distance}')
        paths = []
        while destination:
            paths.append(destination.name)
            destination = destination.prev
        # because the paths starts from destination, so we need to reverse it
        paths.reverse()
        paths = ' -> '.join(paths)
        print(f'the path is {paths}')


if __name__ == '__main__':
    node_a = Node('a')
    node_b = Node('b')
    node_c = Node('c')
    node_d = Node('d')
    node_e = Node('e')
    node_f = Node('f')
    node_g = Node('g')
    node_h = Node('h')
    node_a.add_edge(6, node_b)
    node_a.add_edge(9, node_d)
    node_a.add_edge(10, node_c)
    node_b.add_edge(5, node_d)
    node_b.add_edge(16, node_e)
    node_b.add_edge(13, node_f)
    node_c.add_edge(9, node_d)
    node_c.add_edge(5, node_h)
    node_c.add_edge(21, node_g)
    node_d.add_edge(8, node_f)
    node_d.add_edge(7, node_h)
    node_e.add_edge(10, node_g)
    node_f.add_edge(12, node_g)
    node_f.add_edge(4, node_e)
    node_h.add_edge(14, node_g)

    result = Dijkstras()
    result.get_shorted_path(node_a, node_g)
