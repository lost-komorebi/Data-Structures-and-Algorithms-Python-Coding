#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   graph.py
@Time    :   2023/03/25 20:17:48
@Author  :   komorebi 
'''
from __future__ import annotations
""" graph implementtion by using adjacency list """


class Vertex:
    def __init__(self, name: str):
        self.name = name
        self.neighbors = {}
        self.distance = 0
        self.prev = None  # predecessor
        self.discovery_time = 0  # the number of steps when a vertex is first encountered
        self.finish_time = 0  # the number of steps when a vertex is colored black
        self.color = None

    def add_neighbor(self, name_of_nbr: int | str, weight: int = 0):
        self.neighbors[name_of_nbr] = weight

    def __str__(self):
        return str(self.get_name()) + ' connects to: ' + str([x.get_name() for x in self.neighbors])

    def get_connections(self):
        """ get all adjacency neighbors of current vertex """
        return self.neighbors.keys()

    def get_name(self):
        return self.name

    def get_weight(self, neighbor: Vertex):
        return self.neighbors.get(neighbor)

    def get_distance(self):
        return self.distance

    def set_distance(self, distance):
        self.distance = distance

    def set_prev(self, vertex):
        self.prev = vertex

    def get_prev(self):
        return self.prev

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def set_discovery_time(self, time):
        self.discovery_time = time

    def set_finish_time(self, time):
        self.finish_time = time


class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_of_vertices = 0

    def add_vertex(self, key: str):
        self.num_of_vertices += 1
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        return self.vertices.get(n)

    def __contains__(self, n):
        """ check if a key in graph """
        return n in self.vertices

    def add_edge(self, f: int | str, t: int | str, weight=0):
        """
        f: key of from vertex
        t: key of to vertex
        """
        if f not in self.vertices:
            self.add_vertex(f)
        if t not in self.vertices:
            self.add_vertex(t)
        self.vertices[f].add_neighbor(self.vertices[t], weight)

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())


if __name__ == '__main__':
    g = Graph()
    for i in range(5):
        g.add_vertex(i)
    print(g.vertices)
    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)
    for vertex in g:
        print(vertex)